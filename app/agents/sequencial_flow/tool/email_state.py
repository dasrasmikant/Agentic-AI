from typing import TypedDict
# Define the shared state
class EmailState(TypedDict):
    raw_email: str
    tone: str
    improved_email: str
    reviewed_email: str
