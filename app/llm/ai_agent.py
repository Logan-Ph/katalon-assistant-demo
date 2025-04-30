import json
import os
from langchain_google_genai import GoogleGenerativeAI
from typing import Optional, AsyncGenerator
from dotenv import load_dotenv
from langchain_core.exceptions import *

load_dotenv()

llm = GoogleGenerativeAI(model="gemini-2.5-pro-exp-03-25", google_api_key=os.getenv("GOOGLE_API_KEY"))

async def get_gemini_response(query: str, context: Optional[str] = None):
    """
    Get a response from Gemini based on the query and context.
    
    Args:
        query: User query
        context: Context from RAG if available
        
    Returns:
        Gemini's response
    """
   
    if context:
        prompt = f"""
        As an AI assistant for Katalon documentation, answer the following question
        using the provided context. If the context doesn't contain the information
        needed to answer the question, say that you don't have that information.
        
        Context:
        {context}
        
        Question: {query}
        """
    else:
        prompt = f"""
        As an AI assistant for Katalon documentation, answer the following question
        about Katalon:
        
        Question: {query}
        
        If you don't know the answer, please say so.
        """
    
    response = llm.invoke(prompt)
    
    return response

async def stream_gemini_response(query: str, context: Optional[str] = None) -> AsyncGenerator[str, None]:
    """
    Stream a response from Gemini based on the query and context.
    
    Args:
        query: User query
        context: Context from RAG if available
        
    Yields:
        Chunks of Gemini's response as they become available
    """
    if context:
        prompt = f"""
        As an AI assistant for Katalon documentation, answer the following question
        using the provided context. If the context doesn't contain the information
        needed to answer the question, say that you don't have that information.
        
        Context:
        {context}
        
        Question: {query}
        """
    else:
        prompt = f"""
        As an AI assistant for Katalon documentation, answer the following question
        about Katalon:
        
        Question: {query}
        
        If you don't know the answer, please say so.
        """
    try:
        async for chunk in llm.astream(prompt):
            yield chunk
    except AttributeError as e:
        print(e)
        yield "Attribute error"
    except Exception as e:
        print(e)
        yield "An error occurred while streaming the response."