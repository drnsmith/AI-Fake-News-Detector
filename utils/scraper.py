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

    print(f"Fetching article from: {url}")

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return {"error": f"Request failed: {e}"}

    print("Parsing content with BeautifulSoup...")
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract title
    title_tag = soup.find("title")
    title = title_tag.text if title_tag else "No Title Found"

    # Extract article text
    paragraphs = soup.find_all("p")
    content = " ".join([p.text.strip() for p in paragraphs if p.text.strip()])

    if not content:
        print("No article content found.")
        return {"error": "No article content found"}

    print("Scraping successful!")
    return {"title": title, "content": content[:500]}  # Limit output for readability

# Example Usage (for testing)
if __name__ == "__main__":
    test_url = "https://www.bbc.com/news/world-us-canada-64720072"  # Replace with a real news URL
    article = fetch_news_article(test_url)
    print(article)


