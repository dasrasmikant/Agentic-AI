from app.agents.conditional_flow.etc.complaint_state import ComplaintState
from app.core.llm import gemini_llm

# Step 1: Analyze complaint severity
def classify_severity(state: ComplaintState) -> ComplaintState:
    prompt = f"""
Classify the severity of this customer complaint as 'low', 'medium', or 'high':
Complaint: {state['complaint']}
Only respond with one word: low, medium, or high.
"""
    classification = gemini_llm.invoke(prompt).content.strip().lower()
    return {**state, "severity": classification}