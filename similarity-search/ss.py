import requests, json
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

def my():
    s = requests.Session()
    res = s.get("https://www.myntra.com/sports-shoes/puma/puma-men-blue-hybrid-fuego-running-shoes/11203218/buy", headers=headers, verify=False)

    soup = BeautifulSoup(res.text,"lxml")

    script = None
    for s in soup.find_all("script"):
        if 'pdpData' in s.text:
            script = s.get_text(strip=True)
            break

    a = json.loads(script[script.index('{'):])
    print(a["pdpData"]["productDetails"])


def some():
    s = requests.Session()
    res = s.get("https://www.nykaa.com/twenty-dresses-by-nykaa-fashion-basics-navy-blue-slogan-printed-crop-tshirt/p/6583572?productId=6583572&pps=2&skuId=6583557", verify=False)

    soup = BeautifulSoup(res.text,"lxml")

    script = None
    for s in soup.find_all("script"):
        if 'pdpData' in s.text:
            script = s.get_text(strip=True)
            break

    a = json.loads(script[script.index('{'):])
    print(a)

some()
