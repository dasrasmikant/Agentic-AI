from app.agents.parallel_flow.etc.idea_state import IdeaState
from app.core.llm import gemini_llm
def creative_agent(state: IdeaState) -> IdeaState:
    prompt = f"Come up with a creative idea or metaphor about: {state['topic']}"
    result = gemini_llm.invoke(prompt).content
    return {"thoughts": [f"[Creative] {result}"]}