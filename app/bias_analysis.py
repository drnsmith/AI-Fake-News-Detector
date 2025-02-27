from transformers import pipeline

sentiment_analyser = pipeline("sentiment-analysis")

def analyse_bias(text):
    result = sentiment_analyser(text)
    return result[0]
