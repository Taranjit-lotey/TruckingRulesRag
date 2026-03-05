from openai import OpenAI
from config import OPENAI_API_KEY, CHAT_MODEL, SYSTEM_PROMPT

client = OpenAI(api_key=OPENAI_API_KEY)


def build_context(chunks: list[dict]) -> str:
    """Format retrieved chunks into a context string for the prompt."""
    context_parts = []
    for i, chunk in enumerate(chunks, 1):
        context_parts.append(f"[Source {i} - {chunk['source']}]\n{chunk['text']}")
    return "\n\n---\n\n".join(context_parts)


def generate_answer(query: str, chunks: list[dict]) -> str:
    """
    Generate an answer using the OpenAI Chat API with retrieved context.
    Uses prompt engineering to ground the response in Trucking rules.
    """
    context = build_context(chunks)

    user_prompt = f"""Context from Trucking rules:

{context}

---

Question: {query}

Please answer the question based on the context above. If the context doesn't contain 
enough information, say so clearly."""

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
