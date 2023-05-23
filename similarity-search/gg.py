import requests
from bs4 import BeautifulSoup

def get_page_links(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []

    for link in soup.find_all('a'):
        return link
        href = link.get('href')
        if href and href.startswith('https://www.myntra.com/'):
            links.append(href)

    return links

page_url = 'https://www.myntra.com/clothing?src=bc&p=1'
links = get_page_links(page_url)

for link in links:
    print(link)
