import requests
from bs4 import BeautifulSoup
artworks=[]
base_url = "https://collections.louvre.fr/en/recherche?typology%5B0%5D=1&page={}"
total_pages = 534
for page_number in range(1, total_pages + 1):
    URL = base_url.format(page_number)
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, "html.parser")   
    painting_ = soup.find_all("h3", class_="card__title")
    for painting in painting_:
        p=(painting.text.strip())
        print(p)
        artworks.append(p)







