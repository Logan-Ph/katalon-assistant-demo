import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", google_api_key=os.getenv("GOOGLE_API_KEY"))

async def get_embeddings(query: str, context: Optional[str] = None):
    """
    Generate embeddings for the given text using Google's embedding model.
    
    Args:
        query: The text to generate embeddings for
        context: Optional additional context
        
    Returns:
        The generated embeddings
    """
    if context:
        text_to_embed = f"{query}\n\nContext: {context}"
    else:
        text_to_embed = query
    
    result = embeddings.embed_query(text_to_embed)
    return result
   