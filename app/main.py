from fastapi import FastAPI
from app.routes import pest, disease, soil
from app.auth import routes as auth_routes
from app.db.models import init_db

app = FastAPI(title="AgroSenseAI Backend")

@app.on_event("startup")
def startup():
    init_db()

app.include_router(disease.router, prefix="/disease")
app.include_router(pest.router, prefix="/pest")
app.include_router(soil.router, prefix="/predict")
app.include_router(auth_routes.router, prefix="/auth")