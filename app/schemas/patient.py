from pydantic import BaseModel

class PatientData(BaseModel):
    model_type: str

    Age: float
    Sex: float
    BMI: float
    Waist: float

    Glucose: float | None = None
    Triglycerides: float | None = None

    HDL: float | None = None
    Systolic_BP: float | None = None
    Diastolic_BP: float | None = None