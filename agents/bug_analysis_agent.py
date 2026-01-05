from dotenv import load_dotenv
import os
import json
from groq import Groq
from utils.schemas import BugAnalysisResult

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are a senior QA engineer.

From the bug report below, extract:
- steps_to_reproduce (string or null)
- platform (Android / iOS / Web / Unknown)
- device (device model if mentioned, else null)
- app_version (if mentioned, else null)
- severity (Critical, High, Medium, Low)

Severity rules:
- App crash, data loss, login failure → Critical
- Major functionality broken → High
- Performance or intermittent issue → Medium
- Minor UI issue → Low

Return STRICT JSON ONLY:
{
  "steps_to_reproduce": "...",
  "platform": "...",
  "device": "...",
  "app_version": "...",
  "severity": "..."
}
"""

def analyze_bug(text: str) -> BugAnalysisResult:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ],
        temperature=0
    )

    parsed = json.loads(response.choices[0].message.content)

    return BugAnalysisResult(
        steps_to_reproduce=parsed.get("steps_to_reproduce"),
        platform=parsed.get("platform"),
        device=parsed.get("device"),
        app_version=parsed.get("app_version"),
        severity=parsed["severity"]
    )
