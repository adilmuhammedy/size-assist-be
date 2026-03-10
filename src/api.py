from fastapi import FastAPI
from schemas import (
    BodyRequest,
    BodyResponse,
    CompleteEvaluationRequest,
    CompleteEvaluationResponse
)
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from estimation import predict_body
from ranking import generate_ranking
from recommendation import select_best_size
from size_charts import UNIFIED_SIZE_CHART

app = FastAPI(
    title="SizeAssist API",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# --------------------------------
# PURE ML ESTIMATION
# --------------------------------
@app.post("/predict", response_model=BodyResponse, tags=["Estimation"])
def predict(data: BodyRequest):
    return predict_body(data.height, data.weight, data.gender)




# --------------------------------
# COMPLETE SIZE EVALUATION
# --------------------------------
@app.post("/complete-size-evaluation")
def complete_evaluation(data: CompleteEvaluationRequest):

    apparel = data.apparelType.lower()

    if apparel not in UNIFIED_SIZE_CHART:
        raise HTTPException(status_code=400, detail="Apparel type not supported")

    size_chart = UNIFIED_SIZE_CHART[apparel]

    body = predict_body(
        data.height,
        data.weight,
        data.gender
    )

    ranked_sizes = generate_ranking(
        body,
        size_chart
    )

    recommendation = select_best_size(
        ranked_sizes,
        data.tightnessPreference
    )

    return {
        "recommendedSize": recommendation["recommendedSize"],
        "goodFit": recommendation["goodFit"],
        "rankedSizes": ranked_sizes,
        "bodyMeasurements": body
    }