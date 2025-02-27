from fastapi import FastAPI
from utils.save_html import save_html
from utils.extract_text import extract_article_text

app = FastAPI()

@app.get("/scrape/")
def scrape_article(url: str):
    """
    Scrape a news article from the given URL.
    """
    # Step 1: Fetch and save the HTML
    save_result = save_html(url)

    if "error" in save_result:
        return {"error": save_result["error"]}

    # Step 2: Extract the text
    article = extract_article_text()

    if "error" in article:
        return {"error": article["error"]}

    return {
        "title": article["title"],
        "content": article["content"][:2000]  # Limit content preview
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
