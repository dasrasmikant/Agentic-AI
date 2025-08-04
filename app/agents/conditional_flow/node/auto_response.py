from app.core.llm import gemini_llm
from app.agents.conditional_flow.etc.complaint_state import ComplaintState

# Step 2a: Auto-response for low severity
def auto_response(state: ComplaintState) -> ComplaintState:
    prompt = f"Write a polite auto-response to the customer for this low-severity complaint:\n\n{state['complaint']}"
    response = gemini_llm.invoke(prompt).content
    return {**state, "response": response}