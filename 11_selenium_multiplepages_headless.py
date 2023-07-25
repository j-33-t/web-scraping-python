from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import re
import pandas as pd
from datetime import datetime

options = Options()
options.add_argument('--headless')
options.add_argument('window-size=1920x1080')
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"  # Replace with the actual path to your Chrome binary

# USING CHROME, since safari does not have a headless option
# Instantiate the Chrome driver with the specified options
driver = webdriver.Chrome(options=options)

driver.get('https://www.audible.com/adblbestsellers?ref=a_search_t1_navTop_pl0cg1c0r0&pf_rd_p=08b836ae-73e5-4c8c-9a3d-71c5be252964&pf_rd_r=4BVSZM9W05FH4S9RFT3G&pageLoadId=PHyFqlUBihq8ThKX&creativeId=1642b4d1-12f3-4375-98fa-4938afc1cedc')


#Pagination
pagination = driver.find_element(By.XPATH,'//ul[contains(@class,"pagingElements")]')
pages = pagination.find_elements(By.TAG_NAME,'li')

last_page = int(pages[-2].text)

current_page = 1

book_title = []
author_1 = []
release_date = []

while current_page <= last_page:
    time.sleep(2)
    # # Find all the <a> elements that match the XPath
    # products = driver.find_elements(By.XPATH,'//li')
    # book_title_xpath = 'h3/a'
    # author_1_xpath = 'span[contains(text(),"By:")]/a[1]'
    # release_date_xpath = './/li[contains(@class, "releaseDateLabel")]/span'
    # regex_date_pattern = r"\d{2}-\d{2}-\d{2}"
    

    # for product in products:
    #     # Extract book title
    #     title = product.find_elements(By.XPATH, book_title_xpath)
    #     if title:
    #         book_title.append(title[0].text)
        
    #     # Extract first author
    #     name1 = product.find_elements(By.XPATH, author_1_xpath)
    #     if name1:
    #         author_1.append(name1[0].text)
        
    #     # Extract release date
    #     book_date = product.find_elements(By.XPATH, release_date_xpath)
    #     if book_date:
    #         release_date.append(datetime.strptime(re.search(regex_date_pattern, book_date[0].text).group(), "%m-%d-%y").strftime("%d%b%Y").upper())

    current_page = current_page + 1
    try:
        next_page = driver.find_element(By.XPATH,'//span[contains(@class,"nextButton")]')
        next_page.click()
    except:
        pass

print(len(book_title))
print(len(author_1))
print(len(release_date))

print(book_title[0])

print(book_title[len(book_title) - 1])

# Create a dictionary with the variables
data = {
    'Book_Title' : book_title,
    'Author' : author_1,
    'Release_Date': release_date
}

# Create a dataframe
df = pd.DataFrame(data)

# Export Data as CSV
df.to_csv('audible_top_sellers.csv', index=False)