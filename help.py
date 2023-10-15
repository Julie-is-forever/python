import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
URL = "https://collections.louvre.fr/en/recherche?typology%5B0%5D=1"

# Send an HTTP GET request to the URL
response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")   
    # Locate the specific HTML elements containing painting names
    painting_elements = soup.find_all("h2", class_="title")
    # Extract and print the names of the paintings
for painting in painting_elements:
    print(painting.text.strip())
else:
    print("Failure")