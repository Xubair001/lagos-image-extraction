import os
from io import BytesIO

import requests
from PIL import Image, ImageFile, UnidentifiedImageError

ImageFile.LOAD_TRUNCATED_IMAGES = True  # Handle truncated images gracefully

# Mapping typeItem codes to folder names
TYPE_MAP = {
    "P": "PARTS",
    "M": "MINIFIGS",
    "S": "SETS",
}


def download_bricklink_images(part_ids, base_dir="downloaded_images"):
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "en-US,en;q=0.9",
        "priority": "u=1, i",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
        "referer": "https://www.bricklink.com/v2/search.page",
    }

    search_url = "https://www.bricklink.com/ajax/clone/search/searchproduct.ajax"

    for part_id in part_ids:
        print(f"\n🔍 Searching BrickLink for: {part_id}")
        try:
            response = requests.get(
                search_url, params={"q": part_id}, headers=headers, timeout=15
            )
            if response.status_code == 200:
                data = response.json()
                try:
                    image_data = data["result"]["typeList"][0]["items"][0]
                    type_item = image_data["typeItem"]
                    id_color_img = image_data["idColorImg"]
                    str_item_no = image_data["strItemNo"]

                    # Only allow P, M, S
                    if type_item not in TYPE_MAP:
                        print(
                            f"⚠️ Skipping {part_id}: Unsupported typeItem '{type_item}'"
                        )
                        continue

                    category = TYPE_MAP[type_item]
                    category_folder = os.path.join(base_dir, category, str_item_no)
                    os.makedirs(category_folder, exist_ok=True)

                    # Download full-size image (without .t1)
                    image_url = f"https://img.bricklink.com/ItemImage/{type_item}N/{id_color_img}/{str_item_no}.png"
                    image_response = requests.get(
                        image_url, headers=headers, timeout=10
                    )

                    if image_response.status_code == 200:
                        try:
                            img = Image.open(BytesIO(image_response.content))
                            img.verify()

                            # Reload after verify
                            img = Image.open(BytesIO(image_response.content))
                            save_path = os.path.join(category_folder, f"{part_id}.png")
                            img.save(save_path)
                            print(f"✅ Image saved: {save_path}")
                        except UnidentifiedImageError:
                            print(f"❌ Unidentified or invalid image for {part_id}")
                        except Exception as e:
                            print(f"❌ Error verifying/saving image for {part_id}: {e}")
                    else:
                        print(
                            f"⚠️ Failed to download image: {image_url} (Status {image_response.status_code})"
                        )
                except (IndexError, KeyError):
                    print(f"❌ Could not parse image data for {part_id}")
            else:
                print(
                    f"❌ Failed request for {part_id} (Status {response.status_code})"
                )
        except Exception as e:
            print(f"❌ Exception occurred while processing {part_id}: {e}")


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
    download_bricklink_images(part_ids)
