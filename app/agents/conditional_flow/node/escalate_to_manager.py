from app.core.llm import gemini_llm
from app.agents.conditional_flow.etc.complaint_state import ComplaintState
# Step 2c: Escalate high severity to manager
def escalate_to_manager(state: ComplaintState) -> ComplaintState:
    prompt = f"This is a high severity complaint. Generate a manager alert message and recommended action:\n\n{state['complaint']}"
    response = gemini_llm.invoke(prompt).content
    return {**state, "response": "[Manager Alert]\n" + response}