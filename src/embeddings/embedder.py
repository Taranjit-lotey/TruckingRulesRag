import chromadb
from chromadb.utils import embedding_functions
from config import OPENAI_API_KEY, EMBEDDING_MODEL, VECTOR_STORE_DIR, CHROMA_COLLECTION_NAME


def get_chroma_collection():
    """Initialize ChromaDB client and return the collection."""
    client = chromadb.PersistentClient(path=VECTOR_STORE_DIR)
    openai_ef = embedding_functions.OpenAIEmbeddingFunction(
        api_key=OPENAI_API_KEY,
        model_name=EMBEDDING_MODEL
    )
    collection = client.get_or_create_collection(
        name=CHROMA_COLLECTION_NAME,
        embedding_function=openai_ef
    )
    return collection

