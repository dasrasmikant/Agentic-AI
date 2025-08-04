from app.core.llm import gemini_llm as llm
# llm = ChatOpenAI(model="gpt-4", temperature=0)

def summarize_answer_node(state):
    result_json = getattr(state, "query_result", None) 
      

    prompt = f"""
Here is a JSON result from a Cube.js query:
{result_json}

Summarize the result in clear natural language.
"""
    response = llm.invoke(prompt)
    return {"summary": response.content.strip()}
