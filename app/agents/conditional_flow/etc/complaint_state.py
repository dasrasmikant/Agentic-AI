from typing import TypedDict, Literal

class ComplaintState(TypedDict):
    complaint: str
    severity: Literal["low", "medium", "high"]
    response: str