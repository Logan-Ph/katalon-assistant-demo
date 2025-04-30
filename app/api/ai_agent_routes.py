from fastapi import APIRouter
from pydantic import BaseModel, Field
import json
from app.llm.ai_agent import get_gemini_response, stream_gemini_response
from app.embeddings.embeddings import get_embeddings
from fastapi.responses import StreamingResponse
import asyncio
import random

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
    "/stream",
    summary="Stream a response from the Katalon knowledge base",
    description="Takes a user query about Katalon and streams the response in chunks."
)
async def stream_query(query: QueryRequest):
    async def generate():
        async for chunk in stream_gemini_response(query.query):
            if isinstance(chunk, str):
                # Stream individual characters
                for char in chunk:
                    yield f"data: {json.dumps({'text': char})}\n\n"
                    # Add a small random delay between characters
                    await asyncio.sleep(random.uniform(0.01, 0.05))
            else:
                # If not a string, stream as is
                yield f"data: {json.dumps({'text': str(chunk)})}\n\n"
                await asyncio.sleep(random.uniform(0.01, 0.03))
    
    return StreamingResponse(
        generate(),
        media_type="text/event-stream"
    )


@router.post(
    "/embed",
    status_code=200,
    summary="Embed a query",
    description="Takes a user query and returns its embeddings."
)
async def embed(query: QueryRequest):
    response = await get_embeddings(query.query)
    return {"response": response}
