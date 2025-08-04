from app.agents.parallel_flow.etc.idea_state import IdeaState
from app.core.llm import gemini_llm
# Reducer node: Summarize all collected thoughts
def summarize_thoughts(state: IdeaState) -> IdeaState:
    thoughts_text = "\n".join(state["thoughts"])
    prompt = f"""Summarize the following diverse thoughts into a concise, 
    actionable idea summary for the topic "{state['topic']}": {thoughts_text}

    Summary:"""
    result = gemini_llm.invoke(prompt).content
    return {**state, "summary": result}