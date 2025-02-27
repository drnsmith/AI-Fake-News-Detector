from fastapi import FastAPI, Body
from fact_checker import check_fact
from bias_analysis import analyse_bias

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the AI Fake News Detector"}

@app.post("/analyse/")
def analyse_text(content: dict = Body(...)):  # ✅ Accept raw dictionary
    text = content.get("content")  # Extract "content" manually
    if not text:
        return {"error": "No content provided"}

    credibility = check_fact(text)
    bias = analyse_bias(text)
    return {"credibility": credibility, "bias": bias}
