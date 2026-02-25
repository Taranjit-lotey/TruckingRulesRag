from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP


def chunk_documents(documents: list[dict]) -> list[dict]:
    """
    Split parsed documents into smaller chunks for embedding.
    Each chunk retains source metadata.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    chunks = []
    for doc in documents:
        split_texts = splitter.split_text(doc["text"])
        for i, chunk_text in enumerate(split_texts):
            chunks.append({
                "text": chunk_text,
                "source": doc["source"],
                "filename": doc["filename"],
                "chunk_index": i
            })

    print(f"Created {len(chunks)} chunks from {len(documents)} document(s).")
    return chunks
