import os
from langchain_google_genai import GoogleGenerativeAI
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=os.getenv("GOOGLE_API_KEY"))

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
