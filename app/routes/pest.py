from fastapi import APIRouter, UploadFile, File
from PIL import Image
from app.services.predict_keras import predict_pest

router = APIRouter()

@router.post("/detect")
async def detect_pest(file: UploadFile = File(...)):
    image = Image.open(file.file)
    result = predict_pest(image)
    return result
