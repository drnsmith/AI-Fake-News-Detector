import openai
import os

# Load API key (replace with your key if using OpenAI directly)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def check_fact(text):
    """
    Uses GPT-4 to verify the credibility of the given text.
    Returns a probability score (0-1) and sources.
    """
    if not OPENAI_API_KEY:
        raise ValueError("OpenAI API key not found. Set it as an environment variable.")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an AI that verifies factual accuracy of text."},
                {"role": "user", "content": f"Analyze this news article and rate its credibility: {text}"}
            ],
            max_tokens=100
        )

        # Extract response
        ai_response = response["choices"][0]["message"]["content"]

        # Example output processing (adjust as needed)
        if "highly credible" in ai_response.lower():
            fact_score = 0.9
        elif "possibly false" in ai_response.lower():
            fact_score = 0.4
        else:
            fact_score = 0.7  # Default mid-confidence

        sources = ["OpenAI GPT-4"]  # Placeholder until external sources are integrated

        return fact_score, sources

    except Exception as e:
        return 0.0, ["Error analyzing text: " + str(e)]

