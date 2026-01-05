from agents.csv_reader_agent import load_all_feedback
from agents.classifier_agent import classify_feedback
from agents.bug_analysis_agent import analyze_bug

if __name__ == "__main__":
    records = load_all_feedback()

    for r in records:
        c = classify_feedback(r.raw_text)
        if c.category == "Bug":
            result = analyze_bug(r.raw_text)
            print(result)
            print("-" * 60)
