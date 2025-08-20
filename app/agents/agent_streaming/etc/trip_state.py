# --- State ---
from typing import TypedDict, List
from typing_extensions import Annotated
from operator import add

class TripState(TypedDict):
    destination: str
    dates: str
    weather: str
    events: Annotated[List[str], add]
    activities: Annotated[List[str], add]
    itinerary: Annotated[List[str], add]
    budget: Annotated[List[str], add]
    approved: bool