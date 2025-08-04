from app.agents.sequencial_flow.tool.email_state import EmailState
from app.core.llm import gemini_llm

# Step 1: Rewrite the email in desired tone
def rewrite_email(state: EmailState) -> EmailState:
    prompt = f"""You are an expert communication assistant.
Rewrite the following email in a {state['tone']} tone:

Email:
{state['raw_email']}

Only return the improved email."""
    
    improved = gemini_llm.invoke(prompt).content
    return {**state, "improved_email": improved}