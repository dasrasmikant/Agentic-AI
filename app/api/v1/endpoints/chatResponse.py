from fastapi import APIRouter, Depends, HTTPException
from app.schemas.agent import QueryRequest, QueryResponse
from app.core.llm import gemini_llm
from app.core.prompts import sql_generate_prompt_template
from fastapi.responses import StreamingResponse
import time
router = APIRouter()

@router.post("/generate_sql", response_model=QueryResponse)
async def generate_sql(request: QueryRequest):
    try:
        prompt = sql_generate_prompt_template.format(question=request.query)        
        sql_response = gemini_llm.predict(prompt)
        return QueryResponse(result=sql_response.strip())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def event_stream():
    for i in range(10):
        time.sleep(1)  # Simulate real-time data
        yield f"data: Message s{i}\n\n"

@router.get("/stream")
async def stream():
    return StreamingResponse(event_stream(), media_type="text/event-stream")


