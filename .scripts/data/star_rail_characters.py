import requests

from core.utils import open_data_file

url = "https://www.prydwen.gg/page-data/star-rail/characters/page-data.json"
r = requests.get(url)
data = r.json()

with open_data_file("star_rail_characters") as f:
    f.write(f"# {url}\n")
    for character in data["result"]["data"]["allCharacters"]["nodes"]:
        f.write(f"{character['name']}\n")
