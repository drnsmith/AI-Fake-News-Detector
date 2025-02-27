from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sys
import os

# Ensure the app module is recognized
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fact_checker import check_fact
from bias_analysis import analyse_bias

app = FastAPI()

# Define request model
class AnalyseRequest(BaseModel):
    content: str

@app.get("/")
def home():
    return {"message": "Welcome to the AI Fake News Detector"}

@app.post("/analyse/")
def analyse_text(request: AnalyseRequest):
    try:
        credibility = check_fact(request.content)
        bias = analyse_bias(request.content)
        return {"credibility": credibility, "bias": bias}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
