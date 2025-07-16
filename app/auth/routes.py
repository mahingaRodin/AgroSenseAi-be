from fastapi import APIRouter, HTTPException, Depends, Header, status
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from app.db import get_db
from app.db.models import Farmer
from app.auth.utils import hash_password, verify_password
from app.auth.token import create_access_token, decode_access_token  # add decode function

router = APIRouter()

class FarmerSignup(BaseModel):
    name: str
    email: EmailStr
    password: str

class FarmerLogin(BaseModel):
    email: EmailStr
    password: str

@router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(farmer: FarmerSignup, db: Session = Depends(get_db)):
    existing = db.query(Farmer).filter(Farmer.email == farmer.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email Already Registered.")

    hashed_pw = hash_password(farmer.password)
    new_farmer = Farmer(name=farmer.name, email=farmer.email, password=hashed_pw)
    db.add(new_farmer)
    db.commit()
    db.refresh(new_farmer)

    return {"message": "Farmer registered successfully", "id": new_farmer.id}

@router.post("/login")
def login(user: FarmerLogin, db: Session = Depends(get_db)):
    farmer = db.query(Farmer).filter(Farmer.email == user.email).first()
    if not farmer or not verify_password(user.password, farmer.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": farmer.email})
    return {"access_token": token, "token_type": "bearer"}

# Optional helper to get current user from token in Authorization header
def get_current_user(authorization: str = Header(...), db: Session = Depends(get_db)):
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication scheme")
        payload = decode_access_token(token)
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")
        user = db.query(Farmer).filter(Farmer.email == email).first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        return user
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
