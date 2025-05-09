import os
from io import BytesIO

import requests
from lxml import etree
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True


class LegoImageScraper:
    def __init__(self, item_ids, base_dir="lego_images"):
        self.item_ids = item_ids
        self.base_dir = base_dir
        self.types = {
            "parts": "PARTS",
            "minifigures": "MINIFIGS",
            "complete-sets": "SETS",
        }
        self.min_width = 448
        self.min_height = 448
        self.max_images_per_item = 5
        self.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "accept-language": "en-US,en;q=0.9",
            "user-agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
            ),
        }

    def fetch_page(self, item_type, item_id):
        url = f"https://www.toypro.com/en/list/{item_type}"
        try:
            response = requests.get(
                url, params={"search": item_id}, headers=self.headers, timeout=15
            )
            if response.status_code == 200 and item_id.lower() in response.text.lower():
                return etree.HTML(response.text)
        except Exception:
            pass  # Silently skip on request errors
        return None

    def extract_image_urls(self, tree):
        srcs = tree.xpath("//li//img[contains(@class,'product-top__image')]/@src")
        data_srcs = tree.xpath(
            "//li//img[contains(@class,'product-top__image')]/@data-src"
        )
        original_srcs = tree.xpath(
            "//li//img[contains(@class,'product-top__image')]/@data-original"
        )
        return list(set(srcs + data_srcs + original_srcs))

    def normalize_url(self, url):
        url = url.strip()
        if url.startswith("//"):
            return "https:" + url
        elif url.startswith("/"):
            return "https://www.toypro.com" + url
        return url

    def upscale_image(self, img):
        width, height = img.size
        if width >= self.min_width and height >= self.min_height:
            return img
        scale = max(self.min_width / width, self.min_height / height)
        new_size = (int(round(width * scale)), int(round(height * scale)))
        return img.resize(new_size, Image.LANCZOS)

    def save_image(self, img, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        img.convert("RGB").save(path, "JPEG")

    def run(self):
        for item_id in self.item_ids:
            print(f"\n🔍 Checking for: {item_id}")
            image_count = 0

            for item_type, folder_name in self.types.items():
                if image_count >= self.max_images_per_item:
                    break

                tree = self.fetch_page(item_type, item_id)
                if tree is None:
                    continue

                image_urls = self.extract_image_urls(tree)
                if not image_urls:
                    continue

                normalized_urls = [self.normalize_url(url) for url in image_urls]

                for idx, url in enumerate(normalized_urls):
                    if image_count >= self.max_images_per_item:
                        break
                    try:
                        res = requests.get(url, headers=self.headers, timeout=10)
                        img = Image.open(BytesIO(res.content))
                        upscaled = self.upscale_image(img)
                        folder_path = os.path.join(self.base_dir, folder_name, item_id)
                        img_path = os.path.join(
                            folder_path, f"{item_id}_{image_count + 1}.jpg"
                        )
                        self.save_image(upscaled, img_path)
                        print(f"✅ Saved {img_path}")
                        image_count += 1
                    except Exception:
                        continue  # silently skip failed images

            if image_count == 0:
                print(f"❌ No images found for {item_id}")


if __name__ == "__main__":
    item_ids = [
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
    scraper = LegoImageScraper(item_ids)
    scraper.run()
