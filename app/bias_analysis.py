from transformers import pipeline

# Load a sentiment analysis model from Hugging Face
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_bias(text):
    """
    Uses NLP to analyze bias and sentiment in the given text.
    Returns a bias score (-1: left, 0: neutral, 1: right) and sentiment.
    """

    # Sentiment Analysis
    sentiment_result = sentiment_pipeline(text[:512])  # Limit input length
    sentiment = sentiment_result[0]['label']  # "POSITIVE" or "NEGATIVE"

    # Placeholder Bias Detection (replace with a real model)
    if "Biden" in text or "climate change" in text:
        bias_score = -1  # Left-leaning
    elif "Trump" in text or "gun rights" in text:
        bias_score = 1  # Right-leaning
    else:
        bias_score = 0  # Neutral

    return bias_score, sentiment

