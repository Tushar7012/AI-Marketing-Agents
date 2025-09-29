from pydantic import BaseModel

class ContentRequest(BaseModel):
    client_id: str
    topic: str
    platform: str = "LinkedIn"

class TaskResponse(BaseModel):
    message: str
    task_id: str