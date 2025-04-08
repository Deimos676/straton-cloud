
from fastapi import FastAPI
from ghl import get_leads
from ai_core import ask_ai

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Stratón Cloud Command Node Online"}

@app.get("/get-leads")
def fetch_leads():
    return get_leads()

@app.post("/ask-ai")
def ai_decision(question: str):
    return {"response": ask_ai(question)}
