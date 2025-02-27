from bs4 import BeautifulSoup

def extract_article_text():
    """
    Reads cnn_article.html and extracts the title and full article content.
    """
    with open("cnn_article.html", "r", encoding="utf-8") as file:
        html = file.read()

    soup = BeautifulSoup(html, "html.parser")

    # Extract Title
    title = soup.find("title").text if soup.find("title") else "No Title Found"

    # Extract Article Content (CNN uses <p> tags inside <div>)
    paragraphs = soup.find_all("p")
    content = "\n".join([p.text.strip() for p in paragraphs if p.text.strip()])

    if not content:
        return {"error": "No article content found"}

    return {"title": title, "content": content}

# Run the extraction
if __name__ == "__main__":
    article = extract_article_text()
    
    print("\nTitle:", article["title"])
    print("\nContent Preview:", article["content"][:1000])  # Print first 1000 characters
