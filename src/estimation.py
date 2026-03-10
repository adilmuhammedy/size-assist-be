import joblib
import numpy as np
from schemas import BodyResponse

model = joblib.load("../models/body_model2.pkl")


def predict_body(height: float, weight: float, age:int, gender: int) -> BodyResponse:
    input_data = np.array([[height, weight, age, gender]])
    prediction = model.predict(input_data)

    return BodyResponse(
        chest=float(prediction[0][0]),
        waist=float(prediction[0][1]),
        shoulder=float(prediction[0][2])
    )