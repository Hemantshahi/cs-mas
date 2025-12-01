import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEN_API_KEY")
genai.configure(api_key=API_KEY)

class LLM_Agent:
    def analyze_message(self, message):
        response = genai.responses.create(
            model="models/text-bison-001",
            prompt=f"Classify this safety incident: {message}"
        )
        return response.text
