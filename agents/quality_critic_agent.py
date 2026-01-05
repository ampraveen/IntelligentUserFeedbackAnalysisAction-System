from utils.schemas import Ticket

MIN_CONFIDENCE = 0.6

def review_ticket(ticket: Ticket) -> dict:
    """
    Review a ticket for quality and consistency.
    Returns a decision dict with status and reasons.
    """

    issues = []

    # Confidence check
    if ticket.confidence < MIN_CONFIDENCE:
        issues.append("Low classification confidence")

    # Title check
    if not ticket.title or len(ticket.title) < 10:
        issues.append("Title too short or missing")

    # Bug-specific checks
    if ticket.category == "Bug":
        if "Steps:" not in ticket.technical_details:
            issues.append("Missing steps to reproduce")
        if ticket.priority not in ["Critical", "High", "Medium", "Low"]:
            issues.append("Invalid bug priority")

    # Feature-specific checks
    if ticket.category == "Feature Request":
        if "Demand Level" not in ticket.technical_details:
            issues.append("Missing demand analysis")

    if issues:
        return {
            "status": "Rejected",
            "issues": issues
        }

    return {
        "status": "Approved",
        "issues": []
    }
