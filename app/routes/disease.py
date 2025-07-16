from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from PIL import Image, UnidentifiedImageError
from app.services.predict_keras import predict_disease
from app.auth.dependencies import get_current_user

router = APIRouter(
    tags=["Crop Disease Detection"],
)

@router.post("/detect")
async def detect_disease(
    file: UploadFile = File(...),
    user: str = Depends(get_current_user)
):
    try:
        image = Image.open(file.file)
    except UnidentifiedImageError:
        raise HTTPException(status_code=400, detail="Invalid image file")

    prediction = predict_disease(image)
    return {
        "user": user,
        "prediction": prediction
    }
