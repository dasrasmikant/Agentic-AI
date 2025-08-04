from langchain.tools import tool
import json

# @tool("summarize_result", return_direct=True)
def summarize_result(result_json: str) -> str:
    try:
        data = json.loads(result_json)
    except json.JSONDecodeError:
        return "Cannot summarize: result is not valid JSON."

    rows = data.get("data", [])
    if not rows:
        return "No results found."

    sample = rows[:3]
    summary = f"Result includes {len(rows)} rows. First few rows:\n"
    for row in sample:
        summary += f"- {row}\n"
    return summary
