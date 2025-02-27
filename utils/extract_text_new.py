from bs4 import BeautifulSoup

def extract_article_text():
    """
    Reads cnn_article.html and extracts title + full article content.
    Returns data as a dictionary.
    """
    try:
        with open("cnn_article.html", "r", encoding="utf-8") as file:
            html = file.read()
    except FileNotFoundError:
        return {"error": "cnn_article.html not found. Run save_html.py first."}

    soup = BeautifulSoup(html, "html.parser")

    # Extract Title
    title = soup.find("title").text if soup.find("title") else "No Title Found"

    # Extract Article Content
    paragraphs = soup.find_all("p")
    content = "\n".join([p.text.strip() for p in paragraphs if p.text.strip()])

    if not content:
        return {"error": "No article content found"}

    return {"title": title, "content": content}
