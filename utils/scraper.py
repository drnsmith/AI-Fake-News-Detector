import requests
from bs4 import BeautifulSoup

def fetch_news_article(url):
    """
    Scrapes a news article from the given URL.
    Extracts the title and main content.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return {"error": f"Request failed: {e}"}

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract title
    title = soup.find("title").text if soup.find("title") else "No Title Found"

    # Extract article text (adjust based on structure)
    paragraphs = soup.find_all("p")
    content = " ".join([p.text for p in paragraphs])

    if not content:
        return {"error": "No article content found"}

    return {"title": title, "content": content}

# Example Usage (for testing)
if __name__ == "__main__":
    test_url = "https://www.bbc.com/news/world-us-canada-64720072"  # Replace with any news link
    article = fetch_news_article(test_url)
    print(article)

