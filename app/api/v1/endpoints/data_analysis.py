from fastapi import APIRouter, Depends, HTTPException
from app.schemas.agent import QueryRequest, QueryResponse,QueryResponseJSON
from app.core.llm import gemini_llm
from app.core.prompts import sql_generate_prompt_template
from fastapi.responses import StreamingResponse
from app.crews.data_analysis_agent.pipeline import run_pipeline
from sse_starlette.sse import EventSourceResponse
from app.crews.data_analysis_agent.lib.log_buffer import log_queue
import asyncio

import time
router = APIRouter()

@router.post("/getQueryResponse", response_model=QueryResponse)
async def query_response(request: QueryRequest):
    try:
        response = {}
        # response['response'] = f"response from Agent. query: {request.query}"
        # await asyncio.sleep(5)  # Simulate processing time
        response = await run_pipeline(request.query)
        # print(f"Response from Agent: {response['response']}")
       
        return QueryResponse(result=response["response"], img=response["img"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        await log_queue.put("Query processing completed.")


async def event_stream():
    for i in range(5):
        await asyncio.sleep(0.1)  # Simulate real-time data
        yield f"data: Message s{i}\n\n"

async def event_generator():
        while True:
            try:
                await asyncio.sleep(0.1)
                message =  await log_queue.get()
                yield f"{message}\n\n"
                await asyncio.sleep(0.1)
                
            except asyncio.QueueEmpty:
                await asyncio.sleep(0.1)

@router.get("/progress-stream")
async def stream():
    return EventSourceResponse(event_generator())
    # return StreamingResponse(event_generator(), media_type="text/event-stream")


