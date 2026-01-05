# agentic-feedback-system
Intelligent User Feedback Analysis and Action System
1. Project Overview
This project implements a multi-agent AI system to automatically analyze user feedback from app reviews
and support emails. The system classifies feedback, extracts actionable insights, generates structured
tickets, and provides a monitoring dashboard for manual overrides. The goal is to improve speed,
consistency, and traceability in feedback handling.
2. Business Problem
Manual processing of user feedback is time-consuming and error-prone. Critical bugs may be missed, feature
requests delayed, and prioritization becomes inconsistent. This system automates the entire pipeline using
Agentic AI principles.
3. Multi-Agent Architecture
• CSV Reader Agent – Reads feedback data from CSV files
• Feedback Classifier Agent – Categorizes feedback (Bug, Feature, Praise, Complaint, Spam)
• Bug Analysis Agent – Extracts technical and severity details
• Feature Extractor Agent – Identifies feature requests and user demand
• Ticket Creator Agent – Generates structured tickets
• Quality Critic Agent – Validates ticket completeness and accuracy
4. Technology Stack
• Python 3.x
• CrewAI – Agent orchestration
• Streamlit – User Interface
• Pandas – Data processing
• CSV – Input/Output storage
5. System Workflow
• Read app reviews and support emails from CSV files
• Classify feedback using NLP-based logic
• Analyze bugs and extract technical details
• Generate structured tickets with priorities
• Review tickets using a Quality Critic Agent
• Store results in output CSV files
• Monitor and override using Streamlit dashboard
6. Outputs Generated
• generated_tickets.csv – Final structured tickets
• processing_log.csv – Processing history
• metrics.csv – Performance and accuracy metrics
• Streamlit Dashboard – Monitoring and manual override UI
7. Conclusion
This capstone project demonstrates a complete Agentic AI system that automates user feedback processing.
By leveraging multiple specialized agents, the solution improves efficiency, consistency, and traceability,
making it suitable for real-world SaaS applications.
