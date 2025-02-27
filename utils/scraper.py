import requests
from bs4 import BeautifulSoup

# CNN Homepage URL
url = "https://edition.cnn.com/"

# Set headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Request the page
response = requests.get(url, headers=headers, timeout=10)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract Title
    title = soup.find("title").text if soup.find("title") else "No Title Found"

    # Extract Meta Description
    description_tag = soup.find("meta", attrs={"name": "description"})
    description = description_tag["content"] if description_tag else "No Description Found"

    # Print the results
    print("Title:", title)
    print("Description:", description)

else:
    print("Failed to fetch the page. Status Code:", response.status_code)
