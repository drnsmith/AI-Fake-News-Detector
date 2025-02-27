from fastapi import FastAPI
from fact_checker import check_fact
from bias_analysis import analyse_bias

app = FastAPI()

@app.on_event("startup")
def load_models():
    global fact_checker, bias_analyser
    fact_checker = check_fact
    bias_analyser = analyse_bias
    print("✅ Models loaded successfully!")

@app.get("/")
def home():
    return {"message": "Welcome to the AI Fake News Detector"}

@app.post("/analyse/")
def analyse_text(content: str):
    credibility = fact_checker(content)
    bias = bias_analyser(content)
    return {"credibility": credibility, "bias": bias}
