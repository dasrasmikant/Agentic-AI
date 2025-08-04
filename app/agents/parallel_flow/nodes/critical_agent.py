from app.agents.parallel_flow.etc.idea_state import IdeaState
from app.core.llm import gemini_llm

def critical_agent(state: IdeaState) -> IdeaState:
    prompt = f"Critically evaluate the downsides or limitations of: {state['topic']}"
    result = gemini_llm.invoke(prompt).content
    return {"thoughts": [f"[Critical] {result}"]}