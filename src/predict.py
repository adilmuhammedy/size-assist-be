import joblib
import numpy as np
model = joblib.load("body_model2.pkl")

# Example: 182cm, 75kg, male
input_data = np.array([[182, 75, 1]])

prediction = model.predict(input_data)

print("Predicted Chest:", prediction[0][0])
print("Predicted Waist:", prediction[0][1])
print("Predicted Shoulder:", prediction[0][2])