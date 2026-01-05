import uuid
from utils.schemas import Ticket

def create_ticket(
    source_record,
    classification,
    bug_analysis=None,
    feature_analysis=None
) -> Ticket:
    """
    Deterministically create an engineering-ready ticket
    """

    # Title logic
    if classification.category == "Bug" and bug_analysis:
        title = f"[Bug] {bug_analysis.severity} - {source_record.raw_text[:50]}"
        priority = bug_analysis.severity
        technical_details = (
            f"Platform: {bug_analysis.platform}\n"
            f"Device: {bug_analysis.device}\n"
            f"App Version: {bug_analysis.app_version}\n"
            f"Steps: {bug_analysis.steps_to_reproduce}"
        )

    elif classification.category == "Feature Request" and feature_analysis:
        title = f"[Feature] {feature_analysis.feature_summary}"
        priority = feature_analysis.suggested_priority
        technical_details = (
            f"User Intent: {feature_analysis.user_intent}\n"
            f"Demand Level: {feature_analysis.demand_level}"
        )

    else:
        title = f"[{classification.category}] User Feedback"
        priority = "Low"
        technical_details = "No technical details required."

    return Ticket(
        ticket_id=str(uuid.uuid4()),
        title=title,
        category=classification.category,
        priority=priority,
        description=source_record.raw_text,
        technical_details=technical_details,
        source_id=source_record.source_id,
        source_type=source_record.source_type,
        confidence=classification.confidence
    )
