import torch
from torchvision import transforms
from PIL import Image

# Load models once
disease_model = torch.load("app/models/disease_model.pt", map_location="cpu")
disease_model.eval()

def predict_disease(image: Image.Image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])
    tensor = transform(image).unsqueeze(0)
    output = disease_model(tensor)
    prediction = output.argmax(dim=1).item()
    return prediction
