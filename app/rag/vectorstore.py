from langchain_community.vectorstores import FAISS

from app.rag.embeddings import embedding_model


VECTOR_DB_PATH = "app/rag/faiss_index"


db = FAISS.load_local(
    VECTOR_DB_PATH,
    embedding_model,
    allow_dangerous_deserialization=True
    #Without it, modern LangChain often throws:
    #ValueError:
    # The de-serialization relies loading a pickle file.
)