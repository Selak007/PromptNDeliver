from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .database.db import get_db
from .agents.csa import CSA
from pydantic import BaseModel

app = FastAPI(title="CSA Brain", description="Backend for Customer Service Agent System")

# CORS configuration
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    message: str
    customer_id: int = None

@app.get("/")
def read_root():
    return {"message": "CSA Brain is active"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/csa/chat")
def chat_with_csa(input_data: UserInput, db: Session = Depends(get_db)):
    csa = CSA(db)
    response = csa.process_request(input_data.message, input_data.customer_id)
    return response

@app.get("/dashboard/logs")
def get_logs(limit: int = 10, db: Session = Depends(get_db)):
    csa = CSA(db)
    return csa.memory_manager.get_recent_logs(limit)

@app.get("/dashboard/stats")
def get_stats(db: Session = Depends(get_db)):
    csa = CSA(db)
    return csa.memory_manager.get_memory_stats()
