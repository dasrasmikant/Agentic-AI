from crewai import Agent
from app.crews.data_analysis_agent.tools.save_code import save_code

from app.core.llm import crewai_gemini_llm,groq_llm,openai_llm

data_preparation_agent = Agent(
    role="Data Preparation Agent",
    goal="Write data preparation code based on analysis.",
    backstory="Skilled in writing efficient pandas code for data cleaning and transformation.use the final output dataframe as df_result",
    tools=[save_code],
    llm=crewai_gemini_llm,
    verbose=True
)
