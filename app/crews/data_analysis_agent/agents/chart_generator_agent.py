from crewai import Agent
from app.crews.data_analysis_agent.tools.chart_generator import generate_chart_from_code
from app.crews.data_analysis_agent.tools.get_data_code import get_code
from app.core.llm import crewai_gemini_llm,groq_llm,openai_llm

chart_generator_agent = Agent(
            role="Chart Creator",
            goal="execute the python code and save the chart ",
            backstory="Expert executing data visualization python codes.",
            tools=[generate_chart_from_code],
            llm=crewai_gemini_llm,
            verbose=True
        )
