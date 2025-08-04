from typing_extensions import Annotated
from operator import add
from typing import TypedDict

class IdeaState(TypedDict):
    topic: str
    thoughts: Annotated[list[str], add]
    summary: str