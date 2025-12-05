# Phishing Copilot

AI-powered phishing email analyzer using Google Gemini.

## Setup

### Backend
1. pip install -r backend/requirements.txt
2. Copy .env.example to .env and add your GEMINI_API_KEY
3. cd backend && python -m app.main

### Frontend
Open frontend/index.html in browser or serve with Live Server.

## API
- POST /analyze - Analyze email for phishing
- GET /health - Health check

## Features
- Phishing detection using Gemini AI
- Risk level assessment (low/medium/high)
- Suspicious element identification
- Recommended security actions
