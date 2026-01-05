from dotenv import load_dotenv
import os
import json
from groq import Groq
from utils.schemas import FeatureAnalysisResult

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are a senior product manager.

From the feature request below, extract:
- feature_summary
- user_intent
- demand_level (Low, Medium, High)
- suggested_priority (Low, Medium, High)

Guidelines:
- Repeated usability or productivity requests → High demand
- Nice-to-have improvements → Medium
- Personal preference → Low

Return STRICT JSON ONLY:
{
  "feature_summary": "...",
  "user_intent": "...",
  "demand_level": "...",
  "suggested_priority": "..."
}
"""

def analyze_feature(text: str) -> FeatureAnalysisResult:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ],
        temperature=0
    )

    parsed = json.loads(response.choices[0].message.content)

    return FeatureAnalysisResult(
        feature_summary=parsed["feature_summary"],
        user_intent=parsed["user_intent"],
        demand_level=parsed["demand_level"],
        suggested_priority=parsed["suggested_priority"]
    )
