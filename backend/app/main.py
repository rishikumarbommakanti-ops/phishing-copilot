from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.phishing_analyzer import analyze_email, EmailInput, PhishingAnalysis
from app.config import FRONTEND_URL

app = FastAPI(title="Phishing Copilot API", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def read_root():
    return {"message": "Phishing Copilot API v1.0", "status": "online"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/analyze", response_model=PhishingAnalysis)
async def analyze_phishing_email(email: EmailInput):
    return await analyze_email(email)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
