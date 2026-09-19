from app.llm import llm
from app.vectorstore import get_vectorstore


def answer_question(question: str) -> str:
    vectorstore = get_vectorstore()

    documents = vectorstore.similarity_search(question, k=4)

    context = "\n\n---\n\n".join(
        document.page_content for document in documents
    )

    sources = []
    for document in documents:
        source = document.metadata.get("source", "Unknown")
        if source not in sources:
            sources.append(source)

    prompt = f"""
You are an enterprise IT support assistant.

Answer the user's question using ONLY the provided context.

If the answer is not present in the context, say:
"I don't have enough information in the knowledge base to answer that."

Do not invent policies or procedures.

Context:
{context}

User question:
{question}
"""

    response = llm.invoke(prompt)

    source_text = "\n".join(
        f"- {source}" for source in sources
    )

    return f"{response.content}\n\nSources:\n{source_text}"