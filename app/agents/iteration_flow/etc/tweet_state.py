import operator
from typing import Annotated, Literal, TypedDict

class TweetState(TypedDict):
    topic: str
    tweet: str
    lang:str
    evaluation: Literal["approved", "needs_improvement"]
    feedback: str
    iteration: int
    max_iteration: int
    tweet_history: Annotated[list[str], operator.add]
    feedback_history: Annotated[list[str], operator.add] 