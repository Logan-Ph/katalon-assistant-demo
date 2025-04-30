from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
import json
from app.llm.ai_agent import get_gemini_response
from app.embeddings.embeddings import get_embeddings
from typing import List, Dict, Any, Optional

router = APIRouter(tags=['AI Agent'])

class QueryRequest(BaseModel):
    query: str = Field(..., description="The user's query about Katalon documentation", example="How do I create a test case in Katalon Studio?")
   

@router.post(
    "/query",
    status_code=200,
    summary="Query the Katalon knowledge base",
    description="Takes a user query about Katalon, retrieves relevant documentation, and generates a response using Gemini."
)
async def query(query: QueryRequest):
    response = await get_gemini_response(query.query)
    return {"response": response}


@router.post(
    "/embed",
    status_code=200,
    summary="Embed a query",
    description="Takes a user query and returns its embeddings."
)
async def embed(query: QueryRequest):
    response = await get_embeddings(query.query)
    return {"response": response}
