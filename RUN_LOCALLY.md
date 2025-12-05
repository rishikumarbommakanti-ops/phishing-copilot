# Run Phishing Copilot Locally

## Quick Setup (5 minutes)

### 1. Clone Repository
git clone https://github.com/rishikumarbommakanti-ops/phishing-copilot.git
cd phishing-copilot

### 2. Install Dependencies
cd backend
pip install -r requirements.txt
cp .env.example .env
# Add your GEMINI_API_KEY to .env

### 3. Run Backend
python -m app.main
# API runs at http://localhost:8000

### 4. Open Frontend
Open frontend/index.html in browser

## Test with Sample Email
From: secure-verify@bank-account.com
Subject: URGENT: Verify Account Now
Body: Click to verify account: bit.ly/secure-verify

## Gmail Integration Setup
1. Visit: https://console.cloud.google.com
2. Create OAuth2 credentials
3. Download credentials.json
4. Place in backend/ folder
5. Use Gmail API to fetch real emails

## Deploy to Cloud (Free)

**Render.com:**
1. Push to GitHub
2. Connect Render to repo
3. Set GEMINI_API_KEY env
4. Deploy (auto-builds)

**Vercel (Frontend):**
1. Upload frontend/ folder
2. Set API_URL env variable
3. Deploy
