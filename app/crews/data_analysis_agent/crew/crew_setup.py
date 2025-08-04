from crewai import Crew
from app.crews.data_analysis_agent.tasks.tasks import data_preparation_tasks,data_loading_task, table_generator_tasks, chart_generator_tasks
from app.crews.data_analysis_agent.agents.data_loading_agent import data_loading_agent
from app.crews.data_analysis_agent.agents.data_analysis_agent import data_analysis_agent
from app.crews.data_analysis_agent.agents.data_preparation_agent import data_preparation_agent
from app.crews.data_analysis_agent.agents.response_type_decision_agent import response_type_decision_agent
from app.crews.data_analysis_agent.agents.table_generator_agent import table_generator_agent
from app.crews.data_analysis_agent.agents.chart_code_generator_agent import chart_code_generator_agent
from app.crews.data_analysis_agent.agents.chart_generator_agent import chart_generator_agent

def data_loading_crew(user_question):
    """
    Creates a Crew instance for data loading tasks.
    This crew is responsible for loading data from CSV files into a DataFrame.
    """
    tasks = [data_loading_task()]
    return Crew(
        agents=[data_loading_agent],
        tasks=tasks,
        verbose=True,
        memory=False,
        auto_execute=True
    )

def data_analysis_crew(user_question):

    # data_loading_task=data_loading_task()

    tasks = data_preparation_tasks(user_question)
    
    return Crew(
        agents=[
            data_analysis_agent,
            data_preparation_agent,
            response_type_decision_agent            
        ],
        tasks=tasks,
        verbose=True,
        memory=False,
        auto_execute=True
    )

def table_generation_crew(user_question):
    tasks = table_generator_tasks(user_question)
    return Crew(
        agents=[
            table_generator_agent,           
        ],
        tasks=tasks,
        verbose=True,
        memory=False,
        auto_execute=True
    )

def chart_generation_crew(user_question):

    tasks = chart_generator_tasks(user_question)
    return Crew(
        agents=[
            chart_code_generator_agent,
            chart_generator_agent
            
        ],
        tasks=tasks,
        verbose=True,
        memory=False,
        auto_execute=True
    )