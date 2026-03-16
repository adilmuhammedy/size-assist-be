import joblib
import numpy as np
from src.schemas import BodyResponse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR.parent / "models" / "body_model.pkl"
model = joblib.load(MODEL_PATH)



def predict_body(height: float, weight: float, gender: int) -> BodyResponse:
    input_data = np.array([[height, weight, gender]])
    prediction = model.predict(input_data)

    return BodyResponse(
     chest=round(float(prediction[0][0]), 2),
     waist=round(float(prediction[0][1]), 2),
     shoulder=round(float(prediction[0][2]), 2)
)