from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.fact_checker import check_fact
from app.bias_analysis import analyse_bias

app = FastAPI()

class AnalyseRequest(BaseModel):
    content: str

@app.get("/")
def home():
    return {"message": "Welcome to the AI Fake News Detector"}

@app.post("/analyse/")
def analyse_text(request: AnalyseRequest):
    content = request.content
    if not content:
        raise HTTPException(status_code=400, detail="Content cannot be empty")
    credibility = check_fact(content)
    bias = analyse_bias(content)
    return {"credibility": credibility, "bias": bias}

