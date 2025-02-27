from fastapi import FastAPI
from app.fact_checker import check_fact
from app.bias_analysis import analyse_bias

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the AI Fake News Detector"}

@app.post("/analyse/")
def analyse_text(content: str):
    credibility = check_fact(content)
    bias = analyse_bias(content)
    return {"credibility": credibility, "bias": bias}
