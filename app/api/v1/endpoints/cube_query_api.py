from fastapi import APIRouter, Depends, HTTPException
from app.core.llm import gemini_llm
from app.core.prompts import sql_generate_prompt_template
from fastapi.responses import StreamingResponse
from app.crews.data_analysis_agent.pipeline import run_pipeline
from app.crews.my_cube_query_agent.graph.workflow import build_graph

from sse_starlette.sse import EventSourceResponse
from app.crews.data_analysis_agent.lib.log_buffer import log_queue
import asyncio
from pydantic import BaseModel
import time

# Define request and response models
class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    result: str
    summary: str = None  # Optional field for summary if applicable
    img: str = None  # Optional field for image URL if applicable

router = APIRouter()
@router.post("/getCubeQueryResponse", response_model=QueryResponse)
async def query_response(request: QueryRequest):
    try:
        response = {}
        graph = build_graph()        
        result = graph.invoke({"question": str(request.query)})
        return QueryResponse(result= result['query_result'],summary=result['summary'],img="")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        await log_queue.put("Query processing completed.")