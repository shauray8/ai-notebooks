import requests, json
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

def my():
    s = requests.Session()
    res = s.get("https://www.myntra.com/sports-shoes/puma/puma-men-blue-hybrid-fuego-running-shoes/11203218/buy", headers=headers, verify=False)

    soup = BeautifulSoup(res.text,"lxml")
    print(soup)
    script = None
    for s in soup.find_all("script"):
        if 'pdpData' in s.text:
            script = s.get_text(strip=True)
            break

    a = json.loads(script[script.index('{'):])
    print(a["pdpData"]["productDetails"])


def some():
    s = requests.Session()
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
    res = s.get("https://www.myntra.com/clothing?src=bc&p=1", headers = headers, verify=False)

    soup = BeautifulSoup(res.text,"html.parser")

    print(soup)
    script = None
    for s in soup.find_all("script"):
        if 'products' in s.text:
            script = s.get_text(strip=True)
            break

    print(script)
    a = json.loads(script[script.index('{'):])
    print(a)

some()
