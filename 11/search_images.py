#!.venv/bin/python

import requests
from pprint import pprint as pp
import json
import imageio.v2 as imageio
from io import BytesIO
from PIL import Image
from requests.exceptions import HTTPError
import sys
import re

API_KEY="AIzaSyAMFjH_ZwnO2oh1Z1l-MgRtVFYJafXcTJw"
CX="a6f1ec8fa915b46e0"
pattern=r'^[A-Za-z0-9]+$'



def search(i: int, keyword: str) -> None:
    link = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CX}&q={keyword}&searchType=image&imgSize=xlarge&alt=json&num=10&start=1"

    r = requests.get(link)
    n = len(r.json()['items'])

    images = []

    for j in range(n):
        url = r.json()['items'][j]['link']
        print(url)
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
        except HTTPError as e:
    #        print(e)
            pass
        except Exception as e:
            pass
        try:
            pil_img = Image.open(BytesIO(resp.content))
            pil_img = pil_img.convert("RGB")
            images.append(pil_img)

        except Exception as e:
    #        print(f"Failed to process image {i+1}: {url}")
    #        print("Error:", e)
            pass
    for cnt in range(len(images)):
        pil_img = images[cnt]
        ext = pil_img.format.lower() if pil_img.format else "jpg"
        save_path = f"termen_de_cautare_{i}_{cnt+1}.{ext}"
        pil_img.save(save_path)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print(f"usage: {sys.argv[0]} <keyword_1> <keyword_2> ...")
        exit()

    for word in sys.argv[1:]:
        if not re.match(pattern, word):
            print(f"word --| '{word}' |--contains special characters")
            print("do not use forbidden characters!\ntype only alphanumeric characters")
            exit()

    for i, word in enumerate(sys.argv[1:]):
        search(i+1, word)