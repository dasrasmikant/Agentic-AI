from crewai import Agent
from app.core.llm import crewai_gemini_llm,groq_llm,openai_llm
from app.crews.data_analysis_agent.tools.data_profiler import data_profiler
data_analysis_agent = Agent(
    role="Data Analysis Agent",
    goal="Analyze question and define required data preparation steps",
    backstory="Experienced in exploring and profiling data to extract analytical insights from a dataframe",
    tools=[data_profiler],
    llm=crewai_gemini_llm,
    verbose=True
)
