from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from app.services.predict_soil import predict_soil_fertility
from app.auth.dependencies import get_current_user

router = APIRouter(
    tags=["Soil Prediction"]
)

class SoilInput(BaseModel):
    nitrogen: float = Field(..., ge=0)
    phosphorus: float = Field(..., ge=0)
    potassium: float = Field(..., ge=0)

@router.post("/soil")
def predict_soil(
    input: SoilInput,
    user: str = Depends(get_current_user)
):
    result = predict_soil_fertility(
        input.nitrogen,
        input.phosphorus,
        input.potassium
    )
    return {
        "user": user,
        "result": result
    }
