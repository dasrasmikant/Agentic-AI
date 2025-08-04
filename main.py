from fastapi import FastAPI
from app.api.v1.endpoints import chatResponse,data_analysis,cube_query_api
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Include routers
app.include_router(chatResponse.router)
app.include_router(data_analysis.router)
app.include_router(cube_query_api.router)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Project"}
