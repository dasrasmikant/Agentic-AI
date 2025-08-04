from langchain.tools import tool
import requests
import json

# @tool("execute_cube_query", return_direct=True)
def execute_cube_query(query_json: str) -> str:
    """
    Executes a Cube.js query using the provided JSON string.
    Returns the query result as a formatted JSON string or an error message.
    """
    try:
        print(query_json)
        parsed_query = json.loads(query_json)
    except json.JSONDecodeError:
        return "Invalid JSON format. Please provide valid Cube.js query JSON."

    response = requests.post(
        "http://localhost:4000/cubejs-api/v1/load",
        headers={
            "Authorization": "YOUR_CUBEJS_API_TOKEN",
            "Content-Type": "application/json"
        },
        json={"query": parsed_query} 
    )
    if response.status_code == 200:
        data = response.json().get("data", None)
        if data is not None:
            formatted_data = []
            for row in data:
                formatted_row = {}
                for key, value in row.items():
                    # Extract field name after the dot
                    field_name = key.split('.')[-1]
                    # Format field name: camelCase to Title Case with spaces
                    formatted_field = ''.join(
                        [' ' + c if c.isupper() else c for c in field_name]
                    ).strip().title()
                    formatted_row[formatted_field] = value
                formatted_data.append(formatted_row)
            return json.dumps(formatted_data, indent=2)
        else:
            return "No data found in Cube.js response."
    else:
        return f"Query execution failed: {response.status_code} - {response.text}"