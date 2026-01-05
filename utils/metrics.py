import pandas as pd
import os

def compute_metrics(
    actual_path="data/output/generated_tickets.csv",
    expected_path="data/input/expected_classifications.csv"
):
    # Guard: files must exist
    if not os.path.exists(actual_path) or not os.path.exists(expected_path):
        return {
            "classification_accuracy": 0.0,
            "priority_accuracy": 0.0,
            "total_compared": 0
        }

    actual = pd.read_csv(actual_path)
    expected = pd.read_csv(expected_path)

    # Normalize column names
    actual.columns = [c.strip().lower() for c in actual.columns]
    expected.columns = [c.strip().lower() for c in expected.columns]

    # Determine expected column names safely
    category_col = "category"
    expected_category_col = (
        "expected_category"
        if "expected_category" in expected.columns
        else "category"
    )

    priority_col = "priority"
    expected_priority_col = (
        "expected_priority"
        if "expected_priority" in expected.columns
        else "priority"
    )

    # Merge safely
    merged = actual.merge(
        expected,
        on="source_id",
        how="inner",
        suffixes=("_actual", "_expected")
    )

    if merged.empty:
        return {
            "classification_accuracy": 0.0,
            "priority_accuracy": 0.0,
            "total_compared": 0
        }

    # Resolve merged column names
    actual_category = (
        f"{category_col}_actual"
        if f"{category_col}_actual" in merged.columns
        else category_col
    )

    expected_category = (
        f"{expected_category_col}_expected"
        if f"{expected_category_col}_expected" in merged.columns
        else expected_category_col
    )

    actual_priority = (
        f"{priority_col}_actual"
        if f"{priority_col}_actual" in merged.columns
        else priority_col
    )

    expected_priority = (
        f"{expected_priority_col}_expected"
        if f"{expected_priority_col}_expected" in merged.columns
        else expected_priority_col
    )

    classification_accuracy = (
        merged[actual_category] == merged[expected_category]
    ).mean()

    priority_accuracy = (
        merged[actual_priority] == merged[expected_priority]
    ).mean()

    return {
        "classification_accuracy": round(classification_accuracy * 100, 2),
        "priority_accuracy": round(priority_accuracy * 100, 2),
        "total_compared": len(merged)
    }
