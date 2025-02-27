from transformers import pipeline

fact_checker = pipeline("text-classification", model="facebook/bart-large-mnli")

def check_fact(text):
    categories = ["factual", "misleading", "satire"]
    result = fact_checker(text, candidate_labels=categories)
    return max(zip(result["labels"], result["scores"]), key=lambda x: x[1])[0]
