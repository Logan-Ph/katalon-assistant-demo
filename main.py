from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.api import ai_agent_routes
from chainlit.utils import mount_chainlit

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

mount_chainlit(app=app, target="cl_app.py", path="/")