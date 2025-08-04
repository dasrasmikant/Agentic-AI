import json
import re
from app.crews.my_cube_query_agent.tools.load_metadata_tool import load_cube_metadata,load_specific_cube_metadata
from app.core.llm import gemini_llm as llm

def generate_query_node(state):
    question = getattr(state, "question", None)
    metadata = load_specific_cube_metadata('rpt_revenue_data')
    prompt = f"""
Given this Cube.js metadata:
{metadata}

Generate a valid Cube.js query in JSON format to answer the question:
\"{question}\"

**Important:**
- For string filters, use the operator "contains" instead of "equals" to match partial strings.
- Ensure the response is a valid JSON object. Do NOT include any explanation, markdown, or text before or after the JSON.
"""


    response = llm.invoke(prompt)
    raw_response = response.content.strip()

    # Remove markdown backticks if present
    cleaned_json = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw_response.strip(), flags=re.IGNORECASE)

    try:
        cube_query = json.loads(cleaned_json)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse Cube.js query JSON: {e}\nOriginal:\n{cleaned_json}")

    # Return as string for Pydantic compatibility
    return {"cube_query": json.dumps(cube_query)}
