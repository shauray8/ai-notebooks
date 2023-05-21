from selenium import webdriver
from bs4 import BeautifulSoup

# Set the path to the ChromeDriver executable
chrome_driver_path = "/path/to/chromedriver"  # Replace with the actual path to chromedriver

# Set up the Selenium ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run Chrome in headless mode
driver = webdriver.Chrome(chrome_driver_path, options=options)

# Load the webpage
url = "https://www.myntra.com/clothing?src=bc&p=1"
driver.get(url)

# Wait for the content to load (adjust the wait time as needed)
driver.implicitly_wait(5)

# Get the page source after the content is loaded
html_content = driver.page_source

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
print(soup)

# Find and extract the desired information
# Example: Get all the paragraph tags
paragraph_tags = soup.find_all('p')

for p in paragraph_tags:
    print(p.get_text())

# Quit the driver
driver.quit()
