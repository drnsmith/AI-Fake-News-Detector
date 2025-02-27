from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
import threading

app = FastAPI()

# Global variables for lazy model loading
fact_checker = None
bias_analyser = None

# Function to load the model in the background
def load_models():
    global fact_checker, bias_analyser
    from fact_checker import check_fact
    from bias_analysis import analyse_bias
    fact_checker = check_fact
    bias_analyser = analyse_bias
    print("✅ Models loaded successfully!")

# Start loading models in the background
threading.Thread(target=load_models).start()

# Define request model
class AnalyseRequest(BaseModel):
    content: str

@app.get("/")
def home():
    return {"message": "Welcome to the AI Fake News Detector"}

@app.post("/analyse/")
def analyse_text(request: AnalyseRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(load_models)
    if fact_checker and bias_analyser:
        credibility = fact_checker(request.content)
        bias = bias_analyser(request.content)
        return {"credibility": credibility, "bias": bias}
    else:
        return {"message": "Models are still loading. Please try again in a few seconds."}
