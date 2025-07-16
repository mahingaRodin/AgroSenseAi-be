import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image

# Load models
pest_model = load_model("app/models/pest_detector.h5")
disease_model = load_model("app/models/crop_disease_detector.h5")

# Resize target (adjust if your model uses different input shape)
IMG_SIZE = (224, 224)

# Labels
PEST_LABELS = [
    "sawfly", "stem_borer", "grasshopper", "mites", "mosquito",
    "aphids", "army_worms", "bettle", "bollworm"
]

DISEASE_LABELS = [
    "algal", "anthracnose", "bird_eye_spot", "brown_light",
    "gray_light", "healthy", "red_leaf_spot", "white_spot"
]

def prepare_image(image: Image.Image) -> np.ndarray:
    image = image.convert("RGB").resize(IMG_SIZE)
    img_array = img_to_array(image) / 255.0
    return np.expand_dims(img_array, axis=0)

def predict_pest(image: Image.Image):
    input_data = prepare_image(image)
    prediction = pest_model.predict(input_data)[0]
    class_index = np.argmax(prediction)
    return {
        "label": PEST_LABELS[class_index],
        "confidence": float(np.max(prediction)),
        "index": int(class_index)
    }

def predict_disease(image: Image.Image):
    input_data = prepare_image(image)
    prediction = disease_model.predict(input_data)[0]
    class_index = np.argmax(prediction)
    return {
        "label": DISEASE_LABELS[class_index],
        "confidence": float(np.max(prediction)),
        "index": int(class_index)
    }
