from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.loader import load_documents


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )

    return splitter.split_documents(documents)