# SizeAssist API — Local Setup Guide

This guide explains how to run the **SizeAssist API** locally after cloning the repository.

---

# 1. Clone the Repository

```bash
git clone <your-repository-url>
cd sizeassist-api
```

Example:

```bash
git clone https://github.com/your-username/sizeassist-api.git
cd sizeassist-api
```

---

# 2. Create a Virtual Environment

Create a Python virtual environment to isolate dependencies.

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

After activation your terminal should show:

```
(venv)
```

---

# 3. Install Dependencies

Install all required Python packages.

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install fastapi uvicorn scikit-learn pandas joblib
```

---

# 4. Ensure Required Files Exist

The following files must be present in the project.

```
sizeassist-api/
│
├── main.py
├── schemas.py
├── estimation.py
├── ranking.py
├── recommendation.py
├── size_charts.py
├── body_model.pkl
└── requirements.txt
```

Important files:

- `body_model.pkl` → trained ML model
- `size_charts.py` → clothing size charts
- `estimation.py` → body measurement prediction
- `ranking.py` → ranking sizes by fit
- `recommendation.py` → final size selection logic

---

# 5. Run the FastAPI Server

Start the API using **uvicorn**.

```bash
uvicorn main:app --reload
```

Explanation:

```
main  → filename
app   → FastAPI instance
--reload → auto reload when code changes
```

If your file name is different, update accordingly.

Example:

```
uvicorn app:app --reload
```

---

# 6. Access the API

After starting the server you will see:

```
Uvicorn running on http://127.0.0.1:8000
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

This opens the **interactive API documentation** where you can test endpoints.

---

# 7. Available API Endpoints

## 1. Predict Body Measurements

```
POST /predict
```

Predicts chest, waist, and shoulder using height, weight, and gender.

Example Request:

```json
{
  "height": 175,
  "weight": 75,
  "gender": 1
}
```

Example Response:

```json
{
  "chest": 41,
  "waist": 35,
  "shoulder": 19
}
```

---

## 2. Complete Size Evaluation

```
POST /complete-size-evaluation
```

Performs full evaluation including:

- Body measurement prediction
- Size ranking
- Final recommendation

Example Request:

```json
{
  "height": 175,
  "weight": 75,
  "gender": 1,
  "apparelType": "tshirt",
  "tightnessPreference": "regular"
}
```

Example Response:

```json
{
  "recommendedSize": "M",
  "goodFit": true,
  "rankedSizes": [],
  "bodyMeasurements": {
    "chest": 41,
    "waist": 35,
    "shoulder": 19
  }
}
```

---

# 8. API Architecture Overview

```
User Input
   ↓
FastAPI Endpoint
   ↓
Body Estimation (ML Model)
   ↓
Size Ranking Algorithm
   ↓
Fit Preference Adjustment
   ↓
Final Size Recommendation
```

Modules used:

```
schemas.py        → Request & response models
estimation.py     → ML prediction
ranking.py        → Fit scoring
recommendation.py → Size selection logic
size_charts.py    → Clothing measurement data
```

---

# 9. Stopping the Server

Press:

```
CTRL + C
```

to stop the running server.

---

# 10. Troubleshooting

### Module Not Found Error

Install dependencies again:

```bash
pip install -r requirements.txt
```

---

### Model Not Found

Ensure the trained model file exists:

```
body_model.pkl
```

If missing, retrain the model.

---

### Port Already in Use

Run on a different port:

```bash
uvicorn main:app --reload --port 8001
```

---

# 11. Project Purpose

This API powers **SizeAssist**, an AI-based clothing size recommendation system that:

- Predicts body measurements
- Evaluates garment fit
- Recommends optimal clothing size

---

# 12. Example Test Using cURL

```bash
curl -X POST http://127.0.0.1:8000/predict \
-H "Content-Type: application/json" \
-d '{"height":175,"weight":75,"gender":1}'
```

---

# 13. Development Notes

Recommended Python version:

```
Python 3.10+
```

To format code:

```bash
pip install black
black .
```

---

# 14. License

This project is intended for learning and experimentation with ML-powered apparel size prediction.
