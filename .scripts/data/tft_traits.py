from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from core.utils import open_data_file

url = "https://leagueoflegends.fandom.com/wiki/Category:TFT_traits"
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

with open_data_file("tft_traits") as f:
    f.write(f"# {url}\n")
    category = soup.find("div", {"id": "content"}).find(
        "div", {"class": "category-page__members"}
    )
    for a in category.select("a"):
        if a.get("href") and a.string:
            f.write(f"[{a.string[:-20]}](<{urljoin(url, a['href'])}>)\n")
