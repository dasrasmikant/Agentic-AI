from langchain.tools import tool

@tool
def calculator_tool(query: str) -> str:
    """Simple calculator that evaluates expressions like 2+2 or 5*10"""
    try:
        result = eval(query)
        return str(result)
    except:
        return "Invalid expression"