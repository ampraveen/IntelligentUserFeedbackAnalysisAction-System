from agents.csv_reader_agent import load_all_feedback
from agents.classifier_agent import classify_feedback
from agents.bug_analysis_agent import analyze_bug
from agents.feature_extraction_agent import analyze_feature
from agents.ticket_creator_agent import create_ticket

if __name__ == "__main__":
    records = load_all_feedback()

    for r in records:
        classification = classify_feedback(r.raw_text)

        if classification.category == "Bug":
            bug = analyze_bug(r.raw_text)
            ticket = create_ticket(r, classification, bug_analysis=bug)

        elif classification.category == "Feature Request":
            feature = analyze_feature(r.raw_text)
            ticket = create_ticket(r, classification, feature_analysis=feature)

        else:
            ticket = create_ticket(r, classification)

        print(ticket)
        print("-" * 80)
