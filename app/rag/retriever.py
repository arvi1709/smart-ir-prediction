# import chromadb
#
# from app.rag.embeddings import embed_text
#
# client = chromadb.PersistentClient(
#     path="app/rag/chroma_db"
# )
#
# collection = client.get_or_create_collection(
#     name="medical_knowledge"
# )
#
#
# def retrieve_context(query, top_k=5):
#
#     query_embedding = embed_text([query])[0]
#
#     results = collection.query(
#         query_embeddings=[query_embedding],
#         n_results=top_k
#     )
#
#     return results["documents"][0]


from app.rag.vectorstore import db


def retrieve_context(
    query: str,
    k: int = 2
):

    docs = db.similarity_search(
        query,
        k=k
    )

    context = "\n".join(
        doc.page_content
        for doc in docs
    )

    return context
