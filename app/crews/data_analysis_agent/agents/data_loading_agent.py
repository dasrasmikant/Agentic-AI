from crewai import Agent
# from tools.csv_loader import CSVLoaderTool
from app.core.llm import crewai_gemini_llm,groq_llm,openai_llm
from app.crews.data_analysis_agent.tools.csv_loader import csv_loader



data_loading_agent = Agent(
    role="Data Loading Agent",
    goal="Load appropriate data from CSV into a DataFrame for other agents to analyze, based on the user question. show error if receive any error message.",
    backstory="Expert in handling structured data, file parsing, and preparing data for analysis.",
    llm=crewai_gemini_llm,
    tools=[csv_loader],
    verbose=True
)
