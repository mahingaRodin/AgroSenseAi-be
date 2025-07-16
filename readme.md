# 🌱 AgroSenseAI Backend - Crop Disease & Pest Detection API

This is the **backend service** of AgroSenseAI — a smart agriculture system that leverages machine learning to help farmers detect crop diseases and pests from images, and optionally analyze soil fertility using NPK sensor data.

Built with **FastAPI** and **PyTorch**, this backend provides clean and ready-to-use APIs to power modern precision farming solutions.

## 🚀 Features

- 🧠 **Crop Disease & Pest Detection** using ML models
- 📤 **Image Upload API** with predictions in JSON
- 📦 **Dockerized** for easy deployment
- 📚 **Auto-generated API docs** via Swagger (FastAPI)

## 🧰 Backend Tech Stack

- **Backend Framework**: FastAPI
- **Machine Learning**: PyTorch, Torchvision
- **Image Handling**: Pillow
- **API Validation**: Pydantic
- **Containerization**: Docker
- **Deployment**: Render, Railway, or any Docker-supported cloud

## 📁 Project Structure

     app/
    ├── main.py              # FastAPI entry point

├── routes/ # API route handlers
├── services/ # Model prediction logic
├── models/ # Saved ML model files
├── utils/ # Preprocessing tools
├── requirements.txt # Python dependencies
├── Dockerfile # Docker container setup
└── README.md # Project documentation

## 🔌 API Endpoints

| Method | Endpoint          | Description                       |
| ------ | ----------------- | --------------------------------- |
| POST   | `/disease/detect` | Detect crop disease from an image |
| POST   | `/pest/detect`    | Detect pests from a crop image    |
| GET    | `/docs`           | Swagger UI (API documentation)    |

> All image uploads should be sent as `multipart/form-data`

## 🐳 Run with Docker

```bash
# Build Docker image
docker build -t agrosenseai-backend .

# Run container locally
docker run -p 8000:8000 agrosenseai-backend
```

API available at:
👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📦 Run Locally Without Docker

```bash
git clone https://github.com/yourusername/agrosense-backend.git
cd agrosense-backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 🧪 Testing

```bash
pip install pytest
pytest
```

_Add test files under a `tests/` directory._

---

## 📂 Model Format

- Models are stored in `app/models/` directory.
- Accepted formats: `.pt` (PyTorch)
- Models are loaded at runtime for predictions.

---

## 👨‍💻 Maintainer

**ODIIX**
Rwanda Coding Academy
Software Engineer | Embedded & AI Developer

---

## 📜 License

Licensed under the **MIT License**.
See `LICENSE` file for details.

---

## 💡 Backend Mission

> Delivering fast, reliable, and intelligent crop analysis tools for developers and farmers building the future of African agriculture.
