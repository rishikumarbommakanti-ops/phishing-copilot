import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")
