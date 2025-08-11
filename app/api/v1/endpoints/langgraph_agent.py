
import json
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.agents.sequencial_flow.graph.build_graph import invoke_graph
from app.agents.parallel_flow.graph.build_graph import invoke_graph as article_agent_invoke
from app.agents.iteration_flow.graph.build_graph import invoke_graph as tweet_agent_invoke

from app.crews.data_analysis_agent.lib.log_buffer import log_queue

router = APIRouter()
# Pydrantic model for mail rewrite
class QueryResponse(BaseModel):
    result: str

class QueryRequest(BaseModel):
    query: str
    tone: str

# Pydrantic model for article rewrite
class QueryArticleRequest(BaseModel):
    topic:str

class QueryArticleResponse(BaseModel):
    topic: str
    thoughts: list[str]
    summary: str

# Pydrantic model for tweet Generate
class QueryTweetRequest(BaseModel):
    topic: str
    lang:str

class QueryTweetResponse(BaseModel):
    topic: str
    tweet: str
    lang:str
    feedback: str
    tweet_history: list[str]
    feedback_history: list[str]

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


@router.post("/article-write", response_model=QueryArticleResponse)
async def query_response(request: QueryArticleRequest):
    try:
        response = {}       
        response = article_agent_invoke(request.topic)       
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        await log_queue.put("Query processing completed.")

@router.post("/tweet-generate", response_model=QueryTweetResponse)
async def tweet_generate(request: QueryTweetRequest):
    try:
        response = tweet_agent_invoke(request.topic, request.lang)
        # Ensure all required fields are present and correctly mapped
        final_result = {
            "topic": request.topic,
            "tweet": response.get('tweet', ''),
            "lang": request.lang,
            "feedback": response.get('feedback', ''),
            "tweet_history": response.get('tweet_history', []),
            "feedback_history": response.get('feedback_history', [])
        }
        return QueryTweetResponse(**final_result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        await log_queue.put("Tweet generation completed.")
        