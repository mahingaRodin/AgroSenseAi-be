from fastapi import FastAPI
from app.routes import pest, disease

app = FastAPI(title="AgroSenseAI Backend")

app.include_router(disease.router, prefix="/disease")
app.include_router(pest.router, prefix="/pest")
