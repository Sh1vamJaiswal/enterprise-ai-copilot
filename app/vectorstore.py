from langchain_chroma import Chroma

from app.embeddings import embeddings
from app.loader import load_documents
from app.splitting import split_documents


COLLECTION_NAME = "enterprise_knowledge"
PERSIST_DIRECTORY = "data/chroma"


def build_vectorstore():
    """Build the Chroma vector store from the enterprise documents."""
    documents = load_documents()
    chunks = split_documents(documents)

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=PERSIST_DIRECTORY,
    )

    return vectorstore


def get_vectorstore():
    """Load the existing persisted Chroma vector store."""
    return Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=PERSIST_DIRECTORY,
    )