from fastapi import APIRouter, UploadFile, File
from PIL import Image
from app.services.predict_keras import predict_disease

router = APIRouter()

@router.post("/detect")
async def detect_disease(file: UploadFile = File(...)):
    image = Image.open(file.file)
    result = predict_disease(image)
    return result
