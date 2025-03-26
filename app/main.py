from fastapi import FastAPI, HTTPException
from .schemas import User
from .models import fake_user_db

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Wallet API is running"}

@app.post("/register")
def register(user: User):
    if user.username in fake_user_db:
        raise HTTPException(status_code=400, detail="User already exists")
    fake_user_db[user.username] = user.password
    return {"message": "Registered successfully"}

@app.post("/login")
def login(user: User):
    if fake_user_db.get(user.username) != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}

@app.get("/users")
def list_users():
    return list(fake_user_db.keys())
