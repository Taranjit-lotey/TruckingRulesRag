import os
from dotenv import load_dotenv

load_dotenv()

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
EMBEDDING_MODEL = "text-embedding-3-small"
CHAT_MODEL = "gpt-4o"

# Paths
DATA_RAW_DIR = "data/raw"
DATA_PROCESSED_DIR = "data/processed"
VECTOR_STORE_DIR = "vector_store"

# Chunking
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Retrieval
TOP_K = 5

# ChromaDB
CHROMA_COLLECTION_NAME = "truck_rag"

# System prompt
SYSTEM_PROMPT = """You are an expert assistant specializing in truck regulations, compliance rules, 
and transportation law. Answer questions based strictly on the provided context from truck rulebooks, 
DOT regulations, and transportation documents. If the context does not contain enough information to 
answer the question, say so clearly rather than guessing. Always be precise and cite specifics where possible."""
