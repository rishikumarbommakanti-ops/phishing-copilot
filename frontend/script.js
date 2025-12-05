const API_URL = "http://localhost:8000";

document.getElementById("analyzeForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const sender = document.getElementById("sender").value;
    const subject = document.getElementById("subject").value;
    const body = document.getElementById("body").value;
    
    document.getElementById("loading").style.display = "block";
    
    try {
        const response = await fetch(`${API_URL}/analyze`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ sender, subject, body })
        });
        
        const data = await response.json();
        showResults(data);
    } catch (error) {
        alert("Error: " + error);
    }
    
    document.getElementById("loading").style.display = "none";
});

function showResults(data) {
    const badge = document.getElementById("riskBadge");
    badge.className = "risk-badge " + data.risk_level;
    badge.textContent = data.risk_level.toUpperCase() + " RISK";
    
    document.getElementById("phishingStatus").textContent = data.is_phishing ? "🚨 PHISHING" : "✅ SAFE";
    document.getElementById("riskLevel").textContent = data.risk_level;
    document.getElementById("confidence").textContent = (data.confidence * 100).toFixed(0) + "%";
    
    const elements = document.getElementById("suspiciousElements");
    elements.innerHTML = "";
    data.suspicious_elements.forEach(el => {
        const li = document.createElement("li");
        li.textContent = el;
        elements.appendChild(li);
    });
    
    const actions = document.getElementById("recommendedActions");
    actions.innerHTML = "";
    data.recommended_actions.forEach(action => {
        const li = document.createElement("li");
        li.textContent = action;
        actions.appendChild(li);
    });
    
    document.getElementById("results").style.display = "block";
}

function resetForm() {
    document.getElementById("analyzeForm").reset();
    document.getElementById("results").style.display = "none";
}
