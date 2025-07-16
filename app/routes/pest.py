from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from PIL import Image, UnidentifiedImageError
from app.services.predict_keras import predict_pest
from app.auth.dependencies import get_current_user

router = APIRouter(
    tags=["Pest Detection"],
)

@router.post("/detect")
async def detect_pest(
    file: UploadFile = File(...),
    user: str = Depends(get_current_user)
):
    try:
        image = Image.open(file.file)
    except UnidentifiedImageError:
        raise HTTPException(status_code=400, detail="Invalid image file")

    prediction = predict_pest(image)
    return {
        "user": user,
        "prediction": prediction
    }
