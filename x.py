import requests
from bs4 import BeautifulSoup

artworks = []
URL = "https://collections.louvre.fr/en/recherche?typology%5B0%5D=1"
r = requests.get(URL)

if r.status_code == 200:
    soup = BeautifulSoup(r.text, "html.parser")
    painting_elements = soup.find_all("h2", class_="title")
    if painting_elements:
        for painting in painting_elements:
            p = painting.text.strip()
            artworks.append(p)
    else:
        print("No painting elements found on the page. Check the HTML structure.")
else:
    print(f"Failed to retrieve the webpage. Status code: {r.status_code}")

# Print the list of artworks
for artwork in artworks:
    print(artwork)
