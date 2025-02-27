from fastapi import FastAPI
from pydantic import BaseModel
from fact_checker import check_fact
from bias_analysis import analyse_bias

app = FastAPI()

# ✅ Define a proper request model for JSON body parsing
class AnalyseRequest(BaseModel):
    content: str

@app.post("/analyse/")
def analyse_text(request: AnalyseRequest):  # ✅ Expect a JSON request body
    credibility = check_fact(request.content)
    bias = analyse_bias(request.content)
    return {"credibility": credibility, "bias": bias}
