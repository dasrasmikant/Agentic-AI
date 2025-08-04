from crewai import Agent
from app.crews.data_analysis_agent.tools.table_generator import generate_table_from_code
from app.core.llm import crewai_gemini_llm,groq_llm,openai_llm

table_generator_agent = Agent(
    role="Table Generator Agent",
    goal="Use the tool to generate tables based on the user question.",
    backstory="Expert in executing the python codes to generate report based on the user question.",
    tools=[generate_table_from_code],
    llm=crewai_gemini_llm,
    verbose=True,
    allow_delegation=False
)
