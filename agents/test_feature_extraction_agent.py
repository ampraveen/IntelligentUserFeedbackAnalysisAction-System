from agents.csv_reader_agent import load_all_feedback
from agents.classifier_agent import classify_feedback
from agents.feature_extraction_agent import analyze_feature

if __name__ == "__main__":
    records = load_all_feedback()

    for r in records:
        classification = classify_feedback(r.raw_text)
        if classification.category == "Feature Request":
            result = analyze_feature(r.raw_text)
            print("TEXT:", r.raw_text)
            print("SUMMARY:", result.feature_summary)
            print("DEMAND:", result.demand_level)
            print("PRIORITY:", result.suggested_priority)
            print("-" * 60)
