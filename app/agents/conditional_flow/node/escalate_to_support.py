from app.core.llm import gemini_llm
from app.agents.conditional_flow.etc.complaint_state import ComplaintState
# Step 2b: Escalate medium severity
def escalate_to_support(state: ComplaintState) -> ComplaintState:
    prompt = f"Write a message to the support team summarizing this issue:\n\n{state['complaint']}"
    response = gemini_llm.invoke(prompt).content
    return {**state, "response": "[Support Escalation]\n" + response}