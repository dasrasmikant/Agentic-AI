from crewai import Agent
from app.crews.data_analysis_agent.tools.get_data_code import get_code
from app.crews.data_analysis_agent.tools.save_chart_code import save_chart_code
from app.core.llm import crewai_gemini_llm,groq_llm,openai_llm

chart_code_generator_agent = Agent(
            role="Chart Code Creator",
            goal="Write chart generation code in python based on user question.",
            backstory="Get data code from the context and create data visualization code using Python. save the code in the context using tool.",
            tools=[get_code,save_chart_code],
            llm=crewai_gemini_llm,
            verbose=True
        )
