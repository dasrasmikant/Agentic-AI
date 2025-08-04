from crewai import Agent
from app.core.llm import crewai_gemini_llm

qa_assistant_agent = Agent(
    role="QA Assistant Agent",
    goal="Test and validate generated Python code",
    backstory="Quality analyst for Python code, debugging and validating output.",
    tools=[],
    llm=crewai_gemini_llm,
    verbose=True
)
