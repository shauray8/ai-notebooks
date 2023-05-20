import requests
from bs4 import BeautifulSoup


## convert to class maybe

def parse_data(site, URL):

    if site == "myntraa":
        return myntraa(URL)
    if site == "amazon":
        return amazon(URL)
    if site == "ajio":
        return ajio(URL)
    if site == "nykaa":
        return nykaa(URL)

    return None


def myntraa():
    pass

def amazon():
    pass

def ajio():
    pass

def nykaa(URL):
    url = "https://www.nykaa.com/search/result/?q=Clothing"
    response = requests.get(url)
# Create BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
# Find clothing items on the page
    clothing_items = soup.find_all('div', {'class':'css-ifdzs8'})
# Iterate over each clothing item and extract relevant information
    for item in clothing_items:
        # Extract product name
        product_url = item.find('a', {'class': 'css-qlopj4'}).get("href")
        # Print the extracted information
        print("https://www.nykaa.com"+product_url)
        product_response = requests.get("https://www.nykaa.com"+product_url)
        print(product_response)
        product_soup = BeautifulSoup(product_response.text, 'html.parser')
        disc = product_soup.find_all("p")
        print("Product URL:", [disc])
        print("----------------------------------------")
        pass


nykaa("S")
