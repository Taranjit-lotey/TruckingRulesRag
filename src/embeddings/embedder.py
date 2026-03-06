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


def embed_and_store(chunks: list[dict]) -> None:
    """Embed chunks using OpenAI and store them in ChromaDB."""
    collection = get_chroma_collection()

    texts = [chunk["text"] for chunk in chunks]
    ids = [f"{chunk['filename']}_chunk_{chunk['chunk_index']}" for chunk in chunks]
    metadatas = [
        {"source": chunk["source"], "filename": chunk["filename"], "chunk_index": chunk["chunk_index"]}
        for chunk in chunks
    ]

    # Upsert in batches of 100 to avoid rate limits
    batch_size = 100
    for i in range(0, len(texts), batch_size):
        collection.upsert(
            documents=texts[i:i + batch_size],
            ids=ids[i:i + batch_size],
            metadatas=metadatas[i:i + batch_size]
        )
        print(f"  Upserted batch {i // batch_size + 1} ({min(i + batch_size, len(texts))}/{len(texts)} chunks)")

    print(f"Stored {len(chunks)} chunks in ChromaDB collection '{CHROMA_COLLECTION_NAME}'.")
