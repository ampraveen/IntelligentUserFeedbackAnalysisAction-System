import pandas as pd
from utils.schemas import FeedbackRecord


APP_STORE_PATH = "data/input/app_store_reviews.csv"
SUPPORT_EMAIL_PATH = "data/input/support_emails.csv"


def read_app_store_reviews() -> list[FeedbackRecord]:
    df = pd.read_csv(APP_STORE_PATH)
    records = []

    for _, row in df.iterrows():
        records.append(
            FeedbackRecord(
                source_id=row["review_id"],
                source_type="app_store",
                raw_text=row["review_text"],
                metadata=row.to_dict()
            )
        )

    return records


def read_support_emails() -> list[FeedbackRecord]:
    df = pd.read_csv(SUPPORT_EMAIL_PATH)
    records = []

    for _, row in df.iterrows():
        records.append(
            FeedbackRecord(
                source_id=row["email_id"],
                source_type="support_email",
                raw_text=f"{row['subject']} {row['body']}",
                metadata=row.to_dict()
            )
        )

    return records


def load_all_feedback() -> list[FeedbackRecord]:
    feedback = []
    feedback.extend(read_app_store_reviews())
    feedback.extend(read_support_emails())
    return feedback
