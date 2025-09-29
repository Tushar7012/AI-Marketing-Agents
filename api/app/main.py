
from fastapi import FastAPI
from .api import router as api_router

app = FastAPI(
    title="AI Marketing Agents API",
    description="API to manage and trigger marketing agents.",
    version="1.0.0"
)
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"status": "API is running. Go to /docs for the API documentation."}
