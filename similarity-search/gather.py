import requests
from bs4 import BeautifulSoup


def myntraa():
    pass

def amazon():
    pass

def ajio():
    pass

def other():
    pass

# Send a GET request to the Nykaa search page
url = "https://www.nykaa.com/search/result/?q=Clothing"
response = requests.get(url)
# Create BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')
# Find clothing items on the page
clothing_items = soup.find_all('div', {'class': 'css-d5z3ro'})
# Iterate over each clothing item and extract relevant information
for item in clothing_items:
    info = item.find_all('div', {'class': 'item'})
    print(info)
    # Extract product name
    product_name = item.find('a', {'class': 'product-title'}).text.strip()

    # Extract product brand
    product_brand = item.find('a', {'class': 'product-brand'}).text.strip()

    # Extract product price
    product_price = item.find('span', {'class': 'product-price'}).text.strip()

    # Extract product image URL
    product_image_url = item.find('img', {'class': 'product-img'})['src']

    # Extract product URL
    product_url = item.find('a', {'class': 'product-img-link'})['href']

    # Print the extracted information
    print("Product Name:", product_name)
    print("Brand:", product_brand)
    print("Price:", product_price)
    print("Image URL:", product_image_url)
    print("Product URL:", product_url)
    print("----------------------------------------")
