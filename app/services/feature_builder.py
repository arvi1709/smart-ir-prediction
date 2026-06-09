import numpy as np

from app.schemas.patient import PatientData



def build_features(data: PatientData):

    model_type = data.model_type

    if model_type == "basic":

        feature_names = [
            "Age",
            "Sex",
            "BMI",
            "Waist"
        ]

        features = np.array([
            [
                data.Age,
                data.Sex,
                data.BMI,
                data.Waist
            ]
        ])

    elif model_type == "intermediate":

        if data.Glucose is None:
            raise ValueError("Glucose required")

        if data.Triglycerides is None:
            raise ValueError("Triglycerides required")


        feature_names = [
            "Age",
            "Sex",
            "BMI",
            "Waist",
            "Glucose",
            "Triglycerides"
        ]

        features = np.array([
            [
                data.Age,
                data.Sex,
                data.BMI,
                data.Waist,
                data.Glucose,
                data.Triglycerides
            ]
        ])

    elif model_type == "advanced":

        if data.Glucose is None:
            raise ValueError("Glucose required")

        if data.Triglycerides is None:
            raise ValueError("Triglycerides required")

        if data.HDL is None:
            raise ValueError("HDL required")

        if data.HDL == 0:
            raise ValueError("HDL cannot be zero")




        feature_names = [
            "Age",
            "Sex",
            "BMI",
            "Waist",
            "Glucose",
            "Triglycerides",
            "HDL",
            "Systolic_BP",
            "Diastolic_BP"
        ]

        features = np.array([
            [
                data.Age,
                data.Sex,
                data.BMI,
                data.Waist,
                data.Glucose,
                data.Triglycerides,
                data.HDL,
                data.Systolic_BP,
                data.Diastolic_BP
            ]
        ])

    else:
        raise ValueError(
            "Invalid model_type"
        )

    return features, feature_names