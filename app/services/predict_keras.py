import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.layers import DepthwiseConv2D
from PIL import Image

# ✅ Updated custom load function with flexible kwargs handling
def custom_load_model(filepath):
    def custom_depthwise_conv2d(**config):
        config.pop('groups', None)  # Remove unsupported key if present
        return DepthwiseConv2D(**config)

    custom_objects = {'DepthwiseConv2D': custom_depthwise_conv2d}
    return load_model(filepath, custom_objects=custom_objects, compile=False)

# Attempt to load the models
try:
    pest_model = custom_load_model("app/models/pest_detector.h5")
    disease_model = custom_load_model("app/models/crop_disease_detector.h5")
except Exception as e:
    print(f"Error loading models: {e}")
    raise

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

# Image preprocessor
def prepare_image(image: Image.Image) -> np.ndarray:
    image = image.convert("RGB").resize(IMG_SIZE)
    img_array = img_to_array(image) / 255.0
    return np.expand_dims(img_array, axis=0)

# Prediction functions
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
