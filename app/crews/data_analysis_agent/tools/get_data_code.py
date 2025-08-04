from crewai.tools import tool
from app.crews.data_analysis_agent.lib.csv_context import CSVContext, ResultContext, CodeContext

@tool("Python Chart Generator")
def get_code() -> str:
    """
    Get data code from the context.    """
    code = CodeContext.get_code()
    return code
