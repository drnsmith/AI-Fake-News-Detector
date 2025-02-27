import requests
from bs4 import BeautifulSoup

def fetch_cnn_article(url):
    """
    Scrapes a full news article from CNN.
    Extracts title and full text content.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    print(f"Fetching article from: {url}")
    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return {"error": "Failed to fetch article"}

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract Title
    title = soup.find("title").text if soup.find("title") else "No Title Found"

    # Extract Article Text (CNN stores paragraphs inside <div> elements)
    article_divs = soup.find_all("div", class_="zn-body__paragraph")  # Adjust this if needed
    content = " ".join([div.text.strip() for div in article_divs])

    if not content:
        print("Warning: No article content found. Trying <p> tags...")
        paragraphs = soup.find_all("p")
        content = " ".join([p.text.strip() for p in paragraphs])

    if not content:
        return {"error": "No content found"}

    return {"title": title, "content": content}

# Example Usage (Replace URL with a real article)
if __name__ == "__main__":
    test_url = "https://edition.cnn.com/2024/02/27/world/example-news-article/index.html"  # Replace with a real CNN article
    article = fetch_cnn_article(test_url)
    
    print("\nTitle:", article["title"])
    print("\nContent Preview:", article["content"][:1000])  # Print first 1000 characters

