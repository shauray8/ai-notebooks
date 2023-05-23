import requests
from bs4 import BeautifulSoup
import json
from tqdm import trange
import scrapy

def my():
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
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

def actuall_myntraa():

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

def myntraa():
    data = {}
    try:
        with open("raw_data.json") as file:
            data = json.load(file)
    except:
        pass
    for i in trange(500):
        URL = "https://www.flipkart.com/clothing-and-accessories/pr?sid=clo&marketplace=FLIPKART&p%5B%5D=facets.ideal_for%255B%255D%3DWomen&otracker=nmenu_sub_Women_0_Clothing&page={i}"
        #URL = f"https://www.flipkart.com/search?q=clothing&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}"
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
                if data[new] in data:
                    pass
                else:
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


class MySpider(scrapy.Spider):

    name = 'myspider'

    allowed_domains = ['www.myntra.com']

    start_urls = ['https://www.myntra.com/web/v2/search/hat']

    #def start_requests(self):
    #    for tag in self.tags:
    #        for page in range(self.pages):
    #            url = self.url_template.format(tag, page)
    #            yield scrapy.Request(url)

    def parse(self, response):
        print('url:', response.url)

        #print(response.body)

        data = json.loads(response.body)

        print('data.keys():', data.keys())

        print('meta:', data['meta'])

        print("data['data']:", data['data'].keys())

        # download files
        #for href in response.css('img::attr(href)').extract():
        #   url = response.urljoin(src)
        #   yield {'file_urls': [url]}

        # download images and convert to JPG
        #for src in response.css('img::attr(src)').extract():
        #   url = response.urljoin(src)
        #   yield {'image_urls': [url]}

# --- it runs without project and saves in `output.csv` ---

def other_websites():
    from scrapy.crawler import CrawlerProcess

    c = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0',
        #'USER_AGENT': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',

        # save in CSV or JSON
        'FEED_FORMAT': 'csv',     # 'json
        'FEED_URI': 'output.csv', # 'output.json

        # download files to `FILES_STORE/full`
        # it needs `yield {'file_urls': [url]}` in `parse()`
        #'ITEM_PIPELINES': {'scrapy.pipelines.files.FilesPipeline': 1},
        #'FILES_STORE': '/path/to/valid/dir',

        # download images and convert to JPG
        # it needs `yield {'image_urls': [url]}` in `parse()`
        #'ITEM_PIPELINES': {'scrapy.pipelines.files.ImagesPipeline': 1},
        #'IMAGES_STORE': '/path/to/valid/dir',

        #'HTTPCACHE_ENABLED': False,
        #'dont_redirect': True,
        #'handle_httpstatus_list' : [302,307],
        #'CRAWLERA_ENABLED': False,
    })
    c.crawl(MySpider)
    c.start()

if __name__ == "__main__":
    myntraa()
