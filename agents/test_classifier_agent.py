from agents.csv_reader_agent import load_all_feedback
from agents.classifier_agent import classify_feedback

if __name__ == "__main__":
    records = load_all_feedback()

    for r in records[:5]:
        result = classify_feedback(r.raw_text)
        print("TEXT:", r.raw_text[:60])
        print("CATEGORY:", result.category)
        print("CONFIDENCE:", result.confidence)
        print("-" * 50)
