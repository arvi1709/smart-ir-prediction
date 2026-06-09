# from fastapi import APIRouter
#
# from app.schemas.request_model import (
#     PredictionRequest
# )
#
# from app.prediction.predictor import (
#     run_prediction
# )
#
# from app.rag.generator import (
#     generate_explanation
# )
#
# router = APIRouter()
#
#
# @router.post("/predict")
# def predict(request: PredictionRequest):
#
#     prediction_result = run_prediction(
#         request.assessment_type,
#         request.features
#     )
#
#     probability = prediction_result["probability"]
#
#     query = f"""
#     Explain insulin resistance risk with probability:
#     {probability}
#     """
#
#     explanation = generate_explanation(query)
#
#     return {
#         "prediction": prediction_result,
#         "explanation": explanation
#     }

from fastapi import APIRouter
from app.schemas.patient import PatientData
from app.services.prediction_service import predict_patient

router = APIRouter()

@router.post("/predict")
def predict(data: PatientData):
    return predict_patient(data)