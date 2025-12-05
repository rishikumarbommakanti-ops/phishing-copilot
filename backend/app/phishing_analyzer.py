import google.generativeai as genai
from app.config import GEMINI_API_KEY
from pydantic import BaseModel
import json

genai.configure(api_key=GEMINI_API_KEY)

class EmailInput(BaseModel):
    subject: str
    sender: str
    body: str

class PhishingAnalysis(BaseModel):
    is_phishing: bool
    risk_level: str
    confidence: float
    suspicious_elements: list
    recommended_actions: list
    explanation: str

async def analyze_email(email: EmailInput) -> PhishingAnalysis:
    prompt = f"""Analyze this email for phishing indicators.
    Subject: {email.subject}
    From: {email.sender}
    Body: {email.body}
    
    Return JSON: {{"is_phishing": bool, "risk_level": "low|medium|high", "confidence": 0.0-1.0, "suspicious_elements": [], "recommended_actions": [], "explanation": ""}}"""
    
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        result = json.loads(response.text)
        return PhishingAnalysis(
            is_phishing=result.get("is_phishing", False),
            risk_level=result.get("risk_level", "low"),
            confidence=result.get("confidence", 0.5),
            suspicious_elements=result.get("suspicious_elements", []),
            recommended_actions=result.get("recommended_actions", []),
            explanation=result.get("explanation", "Analysis complete")
        )
    except Exception as e:
        return PhishingAnalysis(
            is_phishing=False, risk_level="low", confidence=0.0,
            suspicious_elements=[], recommended_actions=["Error analyzing."],
            explanation=str(e)
        )
