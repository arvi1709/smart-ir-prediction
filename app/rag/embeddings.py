from sentence_transformers import SentenceTransformer


class SentenceTransformersEmbeddings:

    def __init__(self, model_name: str):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts):
        return self.model.encode(
            texts,
            normalize_embeddings=True
        ).tolist()

    def embed_query(self, text):
        return self.model.encode(
            [text],
            normalize_embeddings=True
        )[0].tolist()


embedding_model = SentenceTransformersEmbeddings(
    "sentence-transformers/all-MiniLM-L6-v2"
)


def embed_text(texts):

    embeddings = embedding_model.embed_documents(texts)

    return embeddings
