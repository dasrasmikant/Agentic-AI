from app.agents.parallel_flow.etc.idea_state import IdeaState
from app.core.llm import gemini_llm


def analytical_agent(state: IdeaState) -> IdeaState:
    prompt = f"Give an analytical thought about the topic: {state['topic']}"
    result = gemini_llm.invoke(prompt).content
    return {"thoughts": [f"[Analytical] {result}"]}