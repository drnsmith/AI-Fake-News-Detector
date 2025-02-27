import requests

def save_html(url):
    """
    Fetches a webpage and saves it as cnn_article.html
    Returns success or error message.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code != 200:
        return {"error": f"Failed to fetch page. Status Code: {response.status_code}"}

    with open("cnn_article.html", "w", encoding="utf-8") as file:
        file.write(response.text)

    return {"success": "HTML page saved successfully"}
