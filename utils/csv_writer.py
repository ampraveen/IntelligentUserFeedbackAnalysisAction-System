import csv
from datetime import datetime

def write_generated_tickets(results, filepath="data/output/generated_tickets.csv"):
    with open(filepath, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "ticket_id", "title", "category", "priority",
            "confidence", "status", "issues",
            "source_id", "source_type"
        ])

        for item in results:
            t = item["ticket"]
            r = item["review"]
            writer.writerow([
                t.ticket_id, t.title, t.category, t.priority,
                round(t.confidence, 2), r["status"],
                "; ".join(r["issues"]),
                t.source_id, t.source_type
            ])


def write_processing_log(results, filepath="data/output/processing_log.csv"):
    with open(filepath, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "timestamp", "ticket_id", "category", "status", "notes"
        ])

        for item in results:
            t = item["ticket"]
            r = item["review"]
            writer.writerow([
                datetime.utcnow().isoformat(),
                t.ticket_id,
                t.category,
                r["status"],
                "; ".join(r["issues"]) if r["issues"] else "OK"
            ])
