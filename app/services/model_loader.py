import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MODEL_DIR = os.path.join(
    BASE_DIR,
    "prediction",
    "models"
)

models = {
    "basic": joblib.load(
        os.path.join(MODEL_DIR, "basic.pkl")
    ),

    "intermediate": joblib.load(
        os.path.join(MODEL_DIR, "intermediate.pkl")
    ),

    "advanced": joblib.load(
        os.path.join(MODEL_DIR, "advanced.pkl")
    )
}