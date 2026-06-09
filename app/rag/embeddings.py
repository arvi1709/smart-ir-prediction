import os
from langchain_huggingface import HuggingFaceEmbeddings

token = os.getenv("HF_TOKEN")

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={
            "local_files_only": False,
            "use_auth_token": token
        }
)


def embed_text(texts):

    embeddings = embedding_model.embed_documents(texts)

    return embeddings
