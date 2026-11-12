from typing import Literal

from pydantic import BaseModel


class EmailAnalysis(BaseModel):
    """Structured event information extracted from an email."""

    relevant: bool
    event_type: Literal[
        "interview",
        "work_shift",
        "appointment",
        "event",
        "deadline",
        "other",
    ]
    action: Literal["create", "reschedule", "cancel", "none"]
    title: str | None
    date: str | None
    start_time: str | None
    end_time: str | None
    timezone: str | None
    location: str | None
    needs_review: bool
    action_items:list[str]
