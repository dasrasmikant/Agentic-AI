from crewai.tools import tool
from app.crews.data_analysis_agent.lib.csv_context import CSVContext,ResultContext,ChartCodeContext

@tool("SaveChartCode")
def save_chart_code(code: str) -> str:
    """
    Save chart generation Python code in shared context
    """
    # Save the code to a .py file for record-keeping or debugging
    # with open("E:\\Rasmikant\\projects\\2025\\analyst-agent\\backend2\\app\\crews\\data_analysis_agent\\test\\executed_code.py", "w", encoding="utf-8") as f:
    #     f.write(code)
    ChartCodeContext.set_code(code)
    return "Chart Code Saved in context successfully."
    
