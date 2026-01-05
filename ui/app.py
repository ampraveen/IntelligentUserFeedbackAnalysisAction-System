import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import streamlit as st
import pandas as pd
from orchestration.pipeline import run_pipeline



st.set_page_config(page_title="Agentic Feedback System", layout="wide")

st.title("🧠 Agentic AI – Feedback to Ticket System")

st.markdown(
    """
This dashboard runs a **multi-agent AI pipeline** that:
- Classifies user feedback
- Extracts technical insights
- Creates engineering tickets
- Applies quality governance
"""
)

if st.button("▶ Run Feedback Processing"):
    with st.spinner("Processing feedback using AI agents..."):
        results = run_pipeline()

    rows = []
    for item in results:
        t = item["ticket"]
        r = item["review"]

        rows.append({
            "Ticket ID": t.ticket_id,
            "Title": t.title,
            "Category": t.category,
            "Priority": t.priority,
            "Confidence": round(t.confidence, 2),
            "Status": r["status"],
            "Issues": ", ".join(r["issues"]) if r["issues"] else ""
        })

    df = pd.DataFrame(rows)

    st.success("Processing completed")
    st.dataframe(df, use_container_width=True)

    approved = df[df["Status"] == "Approved"]
    rejected = df[df["Status"] == "Rejected"]

    st.subheader("📊 Summary")
    col1, col2 = st.columns(2)
    col1.metric("Approved Tickets", len(approved))
    col2.metric("Rejected Tickets", len(rejected))
from utils.metrics import compute_metrics

st.subheader("📈 Accuracy Metrics")

if st.button("🔄 Recalculate Metrics"):
    metrics = compute_metrics()

    col1, col2, col3 = st.columns(3)
    col1.metric("Classification Accuracy", f"{metrics['classification_accuracy']}%")
    col2.metric("Priority Accuracy", f"{metrics['priority_accuracy']}%")
    col3.metric("Records Compared", metrics["total_compared"])
else:
    st.info("Run feedback processing first to generate metrics.")
