from typing import List
from pydantic import BaseModel, Field
from typing import Optional, Tuple

# -----------------------------
# Estimation
# -----------------------------
class BodyRequest(BaseModel):
    height: float = Field(..., example=182)
    weight: float = Field(..., example=75)
    gender: int = Field(..., example=1)


class BodyResponse(BaseModel):
    chest: float
    waist: float
    shoulder: float


# -----------------------------
# Size Chart
# -----------------------------
class GarmentSize(BaseModel):
    name: str
    chest: Optional[Tuple[float, float]] = None
    waist: Optional[Tuple[float, float]] = None
    shoulder: Optional[Tuple[float, float]] = None


class CompleteEvaluationRequest(BaseModel):
    height: float
    weight: float
    gender: int
    tightnessPreference: Optional[int] = Field(default=2, ge=0, le=4)
    apparelType: str  


class RankedSize(BaseModel):
    name: str
    recommendationRank: int


class CompleteEvaluationResponse(BaseModel):
    recommendedSize: str
    goodFit: bool
    rankedSizes: List[RankedSize]
    bodyMeasurements: BodyResponse
    

APPAREL_TYPES = {
    "bottomwear",        # jeans/pants/trackpants/joggers/shorts
    "tshirt",            # t-shirts/polos/sweaters/lounge tops
    "formal_shirt",
    "casual_outerwear",  # casual shirts/sweatshirts/hoodies/jackets
    "pyjama",
    "kurta",
    "vest",
    "boxer"
}