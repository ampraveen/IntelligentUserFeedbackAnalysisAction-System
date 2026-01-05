from agents.csv_reader_agent import load_all_feedback


if __name__ == "__main__":
    records = load_all_feedback()
    print(f"Total feedback records loaded: {len(records)}")

    for r in records[:3]:
        print(r)
