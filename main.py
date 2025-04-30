from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from fastapi import APIRouter
from app.api import ai_agent_routes

load_dotenv()
app = FastAPI(
    title="Katalon Documentation Assistant API",
    description="API for retrieving documentation assistance from Katalon knowledge base",
)

app.include_router(ai_agent_routes.router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
async def root():
    return {
        "name": "Katalon Documentation Assistant API",
        "version": "1.0.0",
        "description": "API for retrieving documentation assistance from Katalon knowledge base",
    }

@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return {"status": "healthy", "api_version": "1.0.0"}
