from langchain.tools import tool
import requests

# @tool("load_cube_metadata", return_direct=True)
def load_cube_metadata() -> str:
    """Loads Cube.js metadata schema in JSON string format for LLM use."""
    response = requests.get(
        "http://localhost:4000/cubejs-api/v1/meta",
        headers={"Authorization": "YOUR_CUBEJS_API_TOKEN"}
    )
    if response.status_code == 200:
        return response.text
    else:
        return f"Failed to load metadata: {response.status_code} - {response.text}"

def load_specific_cube_metadata(cube_name: str) -> str:
    """Loads metadata for a specific Cube.js cube in JSON string format."""
    response = requests.get(
        "http://localhost:4000/cubejs-api/v1/meta",
        headers={"Authorization": "YOUR_CUBEJS_API_TOKEN"}
    )
    if response.status_code == 200:
        meta = response.json()
        # Filter cubes by name
        cubes = meta.get("cubes", [])
        cube_meta = next((cube for cube in cubes if cube.get("name") == cube_name), None)
        if cube_meta:
            import json
            return json.dumps(cube_meta)
        else:
            return f"Cube '{cube_name}' not found."
    else:
        return f"Failed to load metadata: {response.status_code} - {response.text}"
