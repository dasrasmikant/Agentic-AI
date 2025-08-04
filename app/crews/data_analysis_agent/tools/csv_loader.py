import pandas as pd
from crewai.tools import tool
from app.crews.data_analysis_agent.lib.csv_context import CSVContext


@tool("CSVLoaderTool")
def csv_loader() -> str:
    """Loads data from CSV file"""
    file_path="E:\\Rasmikant\\projects\\2025\\analyst-agent\\backend2\\app\\crews\\data_analysis_agent\\data\\i3ms_data.csv"
    try:
        df = pd.read_csv(file_path)
        CSVContext.set_result(df)
        return f"CSV loaded successfully with {len(df)} rows and {len(df.columns)} columns."
    except Exception as e:
        CSVContext.set_result(None)
        return f"error loading CSV: {str(e)}"