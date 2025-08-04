from app.agents.sequencial_flow.tool.email_state import EmailState
from app.core.llm import gemini_llm


# Step 2: Review and enhance clarity/politeness
def review_email(state: EmailState) -> EmailState:
    prompt = f"""Review the following email for clarity and politeness. 
Make minor edits if necessary. Return only the improved version.

Email:
{state['improved_email']}"""

    reviewed = gemini_llm.invoke(prompt).content
    return {**state, "reviewed_email": reviewed}