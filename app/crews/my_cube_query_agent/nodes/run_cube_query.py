from app.crews.my_cube_query_agent.tools.cube_query_tool import execute_cube_query

def run_cube_query_node(state):
    cube_query = getattr(state, "cube_query", None)    
    result = execute_cube_query(cube_query)
    return {"query_result": result}
