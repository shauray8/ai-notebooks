import requests
from bs4 import BeautifulSoup
import json
from tqdm import trange

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
    data = {}
    with open("raw_data.json") as file:
        data = json.load(file)
    for i in trange(500):
        URL = f"https://www.flipkart.com/search?q=clothing&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}"
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        clothing_items = soup.find_all('a', class_ = "_2UzuFa")
        for item in trange(len(clothing_items)):
            try:
                new = "https://www.flipkart.com"+clothing_items[item].get("href")
                response = requests.get(new)
                soup = BeautifulSoup(response.content, 'html.parser')
                items = soup.find('div', class_ = "X3BRps").text
                title = soup.find('span', class_ = "B_NuCI").text
                data[new] = title + " " + items
            except:
                pass

        json_data = json.dumps(data)
        with open('raw_data.json', 'w') as file:
            file.write(json_data)

def amazon():
    URL = "https://www.amazon.in/s?k=clothing&i=apparel&ref=nb_sb_noss_1"
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    clothing_items = soup.find_all('div', class_ = ["a-section", "a-spacing-base", "a-text-center"])
    for item in clothing_items:
        pro = item.find_all("a")
        print(pro)
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
        product_response = requests.get("https://www.nykaa.com/rsvp-by-nykaa-fashion-beige-the-power-of-coord-set/p/5216375?productId=5216375&pps=1&skuId=5216351")
        product_soup = BeautifulSoup(product_response.content, 'html.parser')
        print(product_soup.find("div"))
        disc = product_soup.find_all("p", class_ = False)
        
        print("Product URL:", disc)
        print("----------------------------------------")
        pass


if __name__ == "__main__":
    myntraa()
