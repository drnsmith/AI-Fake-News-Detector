from fastapi import FastAPI
from pydantic import BaseModel
from fact_checker import check_fact
from bias_analysis import analyse_bias

app = FastAPI()

# ✅ Define a Pydantic model for request validation
class AnalyseRequest(BaseModel):
    content: str

@app.get("/")
def home():
    return {"message": "Welcome to the AI Fake News Detector"}

@app.post("/analyse/")
def analyse_text(request: AnalyseRequest):  # ✅ Now using a Pydantic model
    credibility = check_fact(request.content)
    bias = analyse_bias(request.content)
    return {"credibility": credibility, "bias": bias}
