from crewai.tools import tool
from app.crews.data_analysis_agent.lib.csv_context import CSVContext, CSVInfoContext
@tool("DataProfilerTool")
def data_profiler():
    """
    Profiles the loaded DataFrame to understand structure, types, and statistics.
    """
    df = CSVContext.get_result()
    try:
        info = {
            "columns": list(df.columns),
            "data_types": df.dtypes.apply(str).to_dict(),
            "null_counts": df.isnull().sum().to_dict(),
            "basic_stats": df.describe(include='all').to_dict()
        }
        CSVInfoContext.set_info(info)
        return info
    except Exception as e:
        return {"error": str(e)}
