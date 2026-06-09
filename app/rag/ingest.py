import os

from langchain_community.document_loaders import (
    PyPDFLoader
)

from langchain_text_splitters import (
    CharacterTextSplitter
)

from langchain_community.vectorstores import (
    FAISS
)

from app.rag.embeddings import (
    embedding_model
)


DATA_DIR = "app/data"
VECTOR_DB_PATH = "app/rag/faiss_index"


def build_vector_store():

    docs = []

    for file in os.listdir(DATA_DIR):

        if file.endswith(".pdf"):

            pdf_path = os.path.join(
                DATA_DIR,
                file
            )

            loader = PyPDFLoader(pdf_path)

            docs.extend(
                loader.load()
            )

    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    documents = splitter.split_documents(
        docs
    )

    vectorstore = FAISS.from_documents(
        documents,
        embedding_model
    )

    vectorstore.save_local(
        VECTOR_DB_PATH
    )

    print(
        f"Indexed {len(documents)} chunks"
    )


if __name__ == "__main__":

    build_vector_store()