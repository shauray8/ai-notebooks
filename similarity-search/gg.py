from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set the path to your chromedriver executable
webdriver_service = Service('path/to/chromedriver')

# Set the options for the Chrome browser
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=webdriver_service, options=options)

# Set the URL of the page to scrape
page_url = 'https://www.myntra.com/clothing?src=bc&p=1'

# Navigate to the page
driver.get(page_url)

# Find all the links on the page
links = driver.find_elements(By.TAG_NAME, 'a')

# Extract the href attribute from each link
page_links = [link.get_attribute('href') for link in links]

# Filter the links to include only those starting with 'https://www.myntra.com/'
myntra_links = [link for link in page_links if link.startswith('https://www.myntra.com/')]

# Print the links
for link in myntra_links:
    print(link)

# Quit the driver
driver.quit()
