from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from utils import get_cors_origins
from services import chat_router, image_router

# Create FastAPI application
app = FastAPI(
    title="Shatably AI",
    description="An interior design assistant application that provides chat-based design advice and image generation capabilities.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=get_cors_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat_router)
app.include_router(image_router)

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to Shatably AI API"}

# Run the application
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)