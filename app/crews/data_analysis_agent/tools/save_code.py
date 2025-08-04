from crewai.tools import tool

from app.crews.data_analysis_agent.lib.csv_context import CSVContext,ResultContext,CodeContext

@tool("SaveCode")
def save_code(code: str) -> str:
    """
    Save Python code in shared context and also write in a python file
    """
    # Save the code to a .py file for record-keeping or debugging
    with open("E:\\Rasmikant\\projects\\2025\\analyst-agent\\backend2\\app\\crews\\data_analysis_agent\\test\\executed_code.py", "w", encoding="utf-8") as f:
        f.write(code)
    CodeContext.set_code(code)
    return "Code Saved in context successfully."
    
