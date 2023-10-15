import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
artworks=[]
URL = "https://collections.louvre.fr/en/recherche?typology%5B0%5D=1"
r = requests.get(URL)
soup = BeautifulSoup(r.text, "html.parser")   
painting_elements = soup.find_all("h2", class_="title")
for painting in painting_elements:
    p=(painting.text.strip())
    artworks.append(p)