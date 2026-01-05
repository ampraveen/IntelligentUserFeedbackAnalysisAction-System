from agents.csv_reader_agent import load_all_feedback
from agents.classifier_agent import classify_feedback
from agents.bug_analysis_agent import analyze_bug
from agents.feature_extraction_agent import analyze_feature
from agents.ticket_creator_agent import create_ticket
from agents.quality_critic_agent import review_ticket
from utils.csv_writer import write_generated_tickets, write_processing_log


def run_pipeline():
    records = load_all_feedback()
    results = []

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

        review = review_ticket(ticket)

        results.append({
            "ticket": ticket,
            "review": review
        })

    # ✅ WRITE CSV OUTPUTS FIRST
    write_generated_tickets(results)
    write_processing_log(results)

    # ✅ THEN RETURN RESULTS
    return results
