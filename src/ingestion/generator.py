from openai import OpenAI
from config import OPENAI_API_KEY, CHAT_MODEL, SYSTEM_PROMPT

client = OpenAI(api_key=OPENAI_API_KEY)


def build_context(chunks: list[dict]) -> str:
    """Format retrieved chunks into a context string for the prompt."""
    context_parts = []
    for i, chunk in enumerate(chunks, 1):
        context_parts.append(f"[Source {i} - {chunk['source']}]\n{chunk['text']}")
    return "\n\n---\n\n".join(context_parts)

