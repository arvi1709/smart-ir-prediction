import numpy as np
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.preprocessing import normalize


class LocalHashingEmbeddings:

    def __init__(self):
        self.vectorizer = HashingVectorizer(
            n_features=384,
            alternate_sign=False,
            norm=None,
            lowercase=True,
            stop_words="english"
        )

    def embed_documents(self, texts):
        matrix = self.vectorizer.transform(texts)
        matrix = normalize(matrix, norm="l2", axis=1)
        return matrix.toarray().astype(np.float32).tolist()

    def embed_query(self, text):
        matrix = self.vectorizer.transform([text])
        matrix = normalize(matrix, norm="l2", axis=1)
        return matrix.toarray().astype(np.float32)[0].tolist()


embedding_model = LocalHashingEmbeddings()


def embed_text(texts):

    embeddings = embedding_model.embed_documents(texts)

    return embeddings
