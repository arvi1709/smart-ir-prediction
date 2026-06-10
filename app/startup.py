import os

def verify_assets():

    required_files = [
        "app/prediction/models/basic.pkl",
        "app/prediction/models/intermediate.pkl",
        "app/prediction/models/advanced.pkl"
    ]

    for file in required_files:

        if not os.path.exists(file):
            raise FileNotFoundError(
                f"Missing required asset: {file}"
            )

    faiss_dir = "app/rag/faiss_index"

    if not os.path.exists(faiss_dir):
        raise FileNotFoundError(
            "FAISS index folder missing"
        )

    if not os.path.exists(".env"):
        print(".env not found; continuing with environment variables")

    print("Startup verification passed")