from dotenv import load_dotenv
import os
import json
from groq import Groq
from utils.schemas import ClassificationResult

# Load environment variables from .env
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
Classify the feedback into EXACTLY ONE category from:
- Bug
- Feature Request
- Praise
- Complaint
- Spam

Return STRICT JSON ONLY in the following format:
{
  "category": "<one category>",
  "confidence": <float between 0 and 1>
}
"""

def classify_feedback(text: str) -> ClassificationResult:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ],
        temperature=0
    )

    # Parse strict JSON response
    parsed = json.loads(response.choices[0].message.content)

    return ClassificationResult(
        category=parsed["category"],
        confidence=float(parsed["confidence"])
    )
