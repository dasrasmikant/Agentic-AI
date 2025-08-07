
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.agents.sequencial_flow.graph.build_graph import invoke_graph
from app.crews.data_analysis_agent.lib.log_buffer import log_queue

router = APIRouter()
class QueryResponse(BaseModel):
    result: str

class QueryRequest(BaseModel):
    query: str
    tone: str

@router.post("/mail-rewrite", response_model=QueryResponse)
async def query_response(request: QueryRequest):
    try:
        response = {}       
        response = invoke_graph(request.query,request.tone)     
       
        return QueryResponse(result=response["reviewed_email"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        await log_queue.put("Query processing completed.")