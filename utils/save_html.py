import requests

# CNN article URL
url = "https://edition.cnn.com/travel/cassowary-worlds-scariest-bird-australia-intl-hnk/index.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers, timeout=10)

if response.status_code == 200:
    with open("cnn_article.html", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("✅ HTML page saved as cnn_article.html")
else:
    print(f"❌ Failed to fetch page. Status Code: {response.status_code}")

