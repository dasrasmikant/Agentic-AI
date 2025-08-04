from crewai import Agent
from app.core.llm import crewai_gemini_llm,groq_llm,openai_llm

response_type_decision_agent = Agent(
    role="Question Response type Identification",
    goal="Determine the type of response required based on the user question.",
    backstory="Expert in classifying user question.",
    tools=[],
    llm=crewai_gemini_llm,
    verbose=True,
    allow_delegation=False
)
