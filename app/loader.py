from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader, TextLoader


DOCUMENTS_PATH = Path("data/documents")


def load_documents():
    loader = DirectoryLoader(
        str(DOCUMENTS_PATH),
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
    )

    return loader.load()