from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="ContentSummarizer",
    description="API for summarizing books and creating content posts.",
    version="0.1.0"
)

app.include_router(router)