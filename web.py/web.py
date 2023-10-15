import requests

# v terminalu pustte: pip install tqdm
from tqdm import tqdm

URL = "https://collections.louvre.fr/en/recherche?typology%5B0%5D=1"
NUMBER_OF_artworks = 10_000_000_000
artworks = []

for number in (pbar := tqdm(range(1, NUMBER_OF_artworks + 1))):
    # print(f"{URL}{number}")
    r = requests.get(url=f"{URL}{number}")
    # print(r)

    lines = r.text.splitlines()
    for line in lines:

        line = line.strip()

        if not line.startswith("<h3"):
            continue
        line = line.replace("<h3>", "")
        line = line.replace("</h3></div>", "")

        pbar.write(line)
        artworks.append(line)