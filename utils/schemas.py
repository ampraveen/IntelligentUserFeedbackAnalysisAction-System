from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class FeedbackRecord:
    source_id: str
    source_type: str   # app_store | support_email
    raw_text: str
    metadata: Dict[str, Any]
@dataclass
class ClassificationResult:
    category: str        # Bug | Feature Request | Praise | Complaint | Spam
    confidence: float    # 0.0 - 1.0
@dataclass
class FeatureAnalysisResult:
    feature_summary: str
    user_intent: str
    demand_level: str   # Low | Medium | High
    suggested_priority: str  # Low | Medium | High
@dataclass
class Ticket:
    ticket_id: str
    title: str
    category: str
    priority: str
    description: str
    technical_details: str
    source_id: str
    source_type: str
    confidence: float
from dataclasses import dataclass
from typing import Optional

@dataclass
class BugAnalysisResult:
    steps_to_reproduce: Optional[str]
    platform: Optional[str]
    device: Optional[str]
    app_version: Optional[str]
    severity: str  # Critical | High | Medium | Low
