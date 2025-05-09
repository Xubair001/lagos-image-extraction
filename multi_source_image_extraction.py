import os
from io import BytesIO

import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageFile, UnidentifiedImageError
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

ImageFile.LOAD_TRUNCATED_IMAGES = True

TYPE_MAP = {"P": "PARTS", "M": "MINIFIGS", "S": "SETS"}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}


def ensure_folder(path):
    os.makedirs(path, exist_ok=True)


def get_next_filename(folder, part_id, ext=".jpg"):
    existing_files = [
        f for f in os.listdir(folder) if f.startswith(part_id) and f.endswith(ext)
    ]
    nums = [
        int(f.replace(part_id + "_", "").replace(ext, ""))
        for f in existing_files
        if f.replace(part_id + "_", "").replace(ext, "").isdigit()
    ]
    next_num = max(nums, default=0) + 1
    return os.path.join(folder, f"{part_id}_{next_num}{ext}")


def save_image(img_url, folder, part_id, ext=".jpg"):
    try:
        response = requests.get(img_url, headers=headers, timeout=10)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            img.verify()
            img = Image.open(BytesIO(response.content))
            save_path = get_next_filename(folder, part_id, ext)
            img.save(save_path)
            print(f"✅ Saved image: {save_path}")
        else:
            print(f"⚠️ Failed to download: {img_url} (Status {response.status_code})")
    except (UnidentifiedImageError, Exception) as e:
        print(f"❌ Error saving {img_url}: {e}")


def get_bricklink_data(part_ids):
    bricklink_data = {}
    for part_id in part_ids:
        print(f"\n🔍 BrickLink: {part_id}")
        try:
            res = requests.get(
                "https://www.bricklink.com/ajax/clone/search/searchproduct.ajax",
                params={"q": part_id},
                headers=headers,
                timeout=15,
            )
            data = res.json()["result"]["typeList"][0]["items"][0]
            type_item = data["typeItem"]
            if type_item not in TYPE_MAP:
                continue
            category = TYPE_MAP[type_item]
            folder = os.path.join("downloaded_images", category)
            if category == "SETS":
                folder = os.path.join(folder, part_id)
            ensure_folder(folder)
            img_url = f"https://img.bricklink.com/ItemImage/{type_item}N/{data['idColorImg']}/{data['strItemNo']}.png"
            folder = os.path.join("downloaded_images", category, part_id)
            ensure_folder(folder)
            save_image(img_url, folder, part_id, ext=".png")

            bricklink_data[part_id] = folder
        except Exception as e:
            print(f"❌ BrickLink error for {part_id}: {e}")
    return bricklink_data


def get_brickowl_images(part_ids, bricklink_data):
    for part_id in part_ids:
        print(f"\n🔍 BrickOwl: {part_id}")
        try:
            url = f"https://www.brickowl.com/search/catalog?query={part_id}"
            res = requests.get(url, headers=headers, timeout=15)
            soup = BeautifulSoup(res.content, "html.parser")
            img_tag = soup.find("a", class_="category-item-image")
            img = img_tag.find("img") if img_tag else None
            if img and img.get("src"):
                img_url = img["src"]
                if img_url.startswith("//"):
                    img_url = "https:" + img_url
                folder = bricklink_data.get(part_id)
                if folder:
                    ensure_folder(folder)
                    save_image(img_url, folder, part_id)
            else:
                print(f"⚠️ No image found for {part_id} on BrickOwl")
        except Exception as e:
            print(f"❌ BrickOwl error for {part_id}: {e}")


def get_brickeconomy_images(part_ids, bricklink_data):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    base_url = "https://www.brickeconomy.com/search?query="
    for part_id in part_ids:
        print(f"\n🔍 BrickEconomy: {part_id}")
        try:
            driver.get(base_url + part_id)
            soup = BeautifulSoup(driver.page_source, "html.parser")
            img_urls = []
            for div in soup.find_all("div", class_="setminifigpanel-img"):
                img = div.find("img")
                if img and img.get("src"):
                    img_urls.append(img["src"])
            for td in soup.find_all("td", class_="hidden-xs ctlsets-image"):
                img = td.find("img")
                if img and img.get("src"):
                    img_urls.append(img["src"])
            for img_url in img_urls:
                if img_url.startswith("/resources"):
                    img_url = "https://www.brickeconomy.com" + img_url
                folder = bricklink_data.get(part_id)
                if folder:
                    ensure_folder(folder)
                    save_image(img_url, folder, part_id)
        except Exception as e:
            print(f"❌ BrickEconomy error for {part_id}: {e}")
    driver.quit()


def download_all_images(part_ids):
    bricklink_data = get_bricklink_data(part_ids)
    get_brickowl_images(part_ids, bricklink_data)
    get_brickeconomy_images(part_ids, bricklink_data)


if __name__ == "__main__":
    part_ids = [
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
    download_all_images(part_ids)
