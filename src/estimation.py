import joblib
import numpy as np
from schemas import BodyResponse

model = joblib.load("../models/body_model.pkl")



def predict_body(height: float, weight: float, gender: int) -> BodyResponse:
    input_data = np.array([[height, weight, gender]])
    prediction = model.predict(input_data)

    return BodyResponse(
     chest=round(float(prediction[0][0]), 2),
     waist=round(float(prediction[0][1]), 2),
     shoulder=round(float(prediction[0][2]), 2)
)