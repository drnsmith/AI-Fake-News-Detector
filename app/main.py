from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.fact_checker import check_fact
from app.bias_analysis import analyze_bias

app = FastAPI()

class ArticleRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "AI Fake News Detector is running!"}

@app.post("/analyze")
def analyze_article(request: ArticleRequest):
    try:
        fact_score, sources = check_fact(request.text)
        bias_score, sentiment = analyze_bias(request.text)

        return {
            "fact_score": fact_score,  # Probability that the article is fake
            "sources": sources,        # Verified sources used
            "bias_score": bias_score,  # Bias rating (left, right, neutral)
            "sentiment": sentiment,    # Sentiment analysis result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
