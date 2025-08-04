from crewai import Task
from app.crews.data_analysis_agent.agents.data_loading_agent import data_loading_agent
from app.crews.data_analysis_agent.agents.data_analysis_agent import data_analysis_agent
from app.crews.data_analysis_agent.agents.data_preparation_agent import data_preparation_agent
from app.crews.data_analysis_agent.agents.table_generator_agent import table_generator_agent
from app.crews.data_analysis_agent.agents.chart_generator_agent import chart_generator_agent
from app.crews.data_analysis_agent.agents.chart_code_generator_agent import chart_code_generator_agent
from app.crews.data_analysis_agent.agents.response_type_decision_agent import response_type_decision_agent
from app.crews.data_analysis_agent.lib.csv_context import CodeContext

code = CodeContext.get_code() if CodeContext.get_code() else "None"
def data_loading_task():
     return Task(
          description="""Understand the user question and load the required CSV file into a pandas dataframe. 
          Use the tool CSVLoaderTool to load the data.""",
          expected_output="Only execute the tool and dont response anything else. If the tool fails, return an error message.",
          agent=data_loading_agent,
     )
def data_preparation_tasks(user_question):
    return [      
        Task(description=f"Analyze the loaded dataframe to determine necessary data preparation steps. question:{user_question}",
             expected_output="A list of data transformation steps required to answer the question.",
             agent=data_analysis_agent,
             ),
          Task(description=
               """Write Python code using pandas based on the transformation steps provided by the data_analysis_agent. question :{user_question}.
               Do not include any code that loads or creates sample data. 
               Assume that the variable `df` is already available in the local context and contains the loaded data. 
               Only focus on transforming or preparing the data as required by the analysis. 
               The code must be syntactically correct and executable within the existing context. 
               Save the generated code in the context using tool for later execution.
               """,
          expected_output="""Save the generated code using tool.""",
          agent=data_preparation_agent,
          ),
           Task(description=
               f"""user question: {user_question}. Analyze the user's question and classify.
                    If the question requires the result in table or report, return 'table_generation'.
                    If the question asks  about chart, graph or plot,  return 'chart_generation'.
                    Return only the intent as a string.
               """,
          expected_output="""response type as 'table_generation' or 'chart_generation'""",
          agent=response_type_decision_agent,
          )
             
         
          ]
def table_generator_tasks(user_question):
     return  [Task(description="""             
             Use the tool to execute the code saved in the context.""",
             expected_output="if the tool is run successfully, return as 'succefully executed'. If the tool return error, show error message.",
             agent=table_generator_agent,
             )]

def chart_generator_tasks(user_question):
     return [
          Task(
    description=f"""User asked: {user_question}

Fetch data preparation code using the tool and append matplotlib code to generate a chart based on the question.

Use `df_result` as the final DataFrame. Do not add code for loading or mocking data.

Constraints:
- Use **only matplotlib** (no plotly).
- Do **not** use `plt.show()` or `fig.show()`.
- Do **not** save the chart to a file.

Store the final code in context using the tool.
""",
    expected_output="Python code that generates a chart using df_result with matplotlib.",
    agent=chart_code_generator_agent
)

,
          Task(
            description=f"""
              Use the tool to execute the code saved in the context.
               """,
            expected_output="if the tool is run successfully, return as 'succefully executed'. If the tool return error, show error message.",
            agent=chart_generator_agent
          )
     ]