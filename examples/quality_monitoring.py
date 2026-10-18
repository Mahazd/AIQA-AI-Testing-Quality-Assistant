"""AIQA selected quality monitoring and human-review logic.

Portfolio excerpt adapted from the local Streamlit prototype.
This is not the complete application or an automated AI accuracy evaluator.
"""

from datetime import datetime
import pandas as pd

REVIEW_CLASSIFICATIONS = [
    "Knowledge Gap", "Retrieval Issue", "Answer Generation Issue",
    "Unclear Question", "Out of Scope", "Other",
]


def quality_summary(feedback: pd.DataFrame) -> dict:
    """Summarize explicitly submitted ratings and review status."""
    required = {"rating", "review_status"}
    missing = required - set(feedback.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")

    rating = feedback["rating"].fillna("").astype(str).str.strip().str.lower()
    status = feedback["review_status"].fillna("").astype(str).str.strip().str.lower()
    positive = rating.isin(["helpful", "yes", "positive", "👍"])
    negative = rating.isin(["not helpful", "no", "negative", "👎"])
    rated = int(positive.sum() + negative.sum())

    return {
        "total_feedback": len(feedback),
        "helpful": int(positive.sum()),
        "not_helpful": int(negative.sum()),
        "helpful_rate_pct": round(100 * int(positive.sum()) / rated, 1) if rated else 0.0,
        "pending_review": int((negative & status.eq("pending review")).sum()),
    }


def top_negative_reasons(feedback: pd.DataFrame, limit: int = 5) -> pd.Series:
    """Return most common reasons attached to negative feedback."""
    if not {"rating", "reason"}.issubset(feedback.columns):
        raise ValueError("Missing required columns: rating, reason")
    rating = feedback["rating"].fillna("").astype(str).str.strip().str.lower()
    negative = rating.isin(["not helpful", "no", "negative", "👎"])
    reasons = feedback.loc[negative, "reason"].fillna("").astype(str).str.strip()
    return reasons[reasons.ne("")].value_counts().head(limit)


def mark_reviewed(
    feedback: pd.DataFrame, row_index: int, classification: str, comment: str
) -> pd.DataFrame:
    """Update an in-memory record; persistence belongs to the application layer."""
    if classification not in REVIEW_CLASSIFICATIONS:
        raise ValueError("Unsupported reviewer classification")
    if row_index not in feedback.index:
        raise KeyError("Feedback row not found")

    result = feedback.copy()
    result.at[row_index, "review_status"] = "Reviewed"
    result.at[row_index, "reviewer_classification"] = classification
    result.at[row_index, "reviewer_comment"] = comment
    result.at[row_index, "reviewed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return result
