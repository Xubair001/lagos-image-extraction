import requests
from bs4 import BeautifulSoup

# Define the search keywords
keywords = [
    "ww016",
    "sw0988",
    "gen060",
    "3007",
    "x224",
    "3069ps1",
    "8095",
    "76251-1",
    "76430-1",
]
# Base URL
base_url = "https://www.brickowl.com/search/catalog?query="
# Dictionary to store results
results = {}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
for keyword in keywords:
    url = base_url + keyword
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    # Find all image containers
    image_tags = soup.find_all("a", class_="category-item-image")
    # Extract the first image URL
    if image_tags:
        img_tag = image_tags[0].find("img")
        img_url = img_tag["src"] if img_tag else "Image not found"
    else:
        img_url = "Image not found"
    results[keyword] = img_url
for k, v in results.items():
    print(f"{k}: {v}")
