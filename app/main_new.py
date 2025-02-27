import sys
import os

# Add the root project directory to Python's path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.save_html_new import save_html_new
from utils.extract_text_new import extract_article_text_new

from fastapi import FastAPI

app = FastAPI()

@app.get("/scrape/")
def scrape_article(url: str):
    """
    Scrape a news article from the given URL.
    """
    # Step 1: Fetch and save the HTML
    save_result = save_html_new(url)

    if "error" in save_result:
        return {"error": save_result["error"]}

    # Step 2: Extract the text
    article = extract_article_text_new()

    if "error" in article:
        return {"error": article["error"]}

    return {
        "title": article["title"],
        "content": article["content"][:2000]  # Limit content preview
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


