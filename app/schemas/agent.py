from pydantic import BaseModel
# Define request and response models
class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    result: str
    img: str = None  # Optional field for image URL if applicable

class QueryResponseJSON(BaseModel):
    result: object  # Assuming the result is a dictionary containing the response data
   