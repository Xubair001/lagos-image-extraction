from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# List of search keywords
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
# Base URL for search
base_url = "https://www.brickeconomy.com/search?query="
# Set up the Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# Function to fetch image URLs for a given keyword
def fetch_image_urls(keyword):
    url = base_url + keyword
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    img_urls = []
    #  check Minifig image
    minifig_divs = soup.find_all("div", class_="setminifigpanel-img")
    for div in minifig_divs:
        img = div.find("img")
        if img and img.get("src"):
            img_urls.append(img["src"])
    # check Set image
    set_tds = soup.find_all("td", class_="hidden-xs ctlsets-image")
    for td in set_tds:
        img = td.find("img")
        if img and img.get("src"):
            img_urls.append(img["src"])
    # Make URLs absolute
    full_img_urls = [
        "https://www.brickeconomy.com" + url if url.startswith("/resources") else url
        for url in img_urls
    ]
    return full_img_urls


for keyword in keywords:
    print(f"Fetching images for: {keyword}")
    img_urls = fetch_image_urls(keyword)
    if img_urls:
        print(f" Found {len(img_urls)} image(s):")
        for url in img_urls:
            print(url)
    else:
        print(" No images found.")
    print("-" * 50)
# Close browser
driver.quit()
