from fastapi import APIRouter, Depends, HTTPException
from fastapi import Request
import httpx
router = APIRouter()

@router.post("/addNum")
async def addNum(request: Request):
    request_data = await request.json()
    n1 = request_data.get("n1")
    n2 = request_data.get("n2")
    if n1 is None or n2 is None:
        raise HTTPException(status_code=400, detail="Missing n1 or n2 in request body")
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://csmfunctionapp.azurewebsites.net/api/add?",
            json={"n1": n1, "n2": n2},
            timeout=10
        )
        response.raise_for_status()
        result = response.json()
        return {"data": result}