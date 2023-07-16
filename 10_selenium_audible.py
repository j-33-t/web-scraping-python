from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time 
import re

# Set up Safari WebDriver
driver = webdriver.Safari()

# Navigate to the website
driver.get("https://www.audible.com/search")

# Maximize the Safari window
driver.maximize_window()


# Find all the <a> elements that match the XPath
products = driver.find_elements(By.XPATH,'//li')

book_title_xpath = 'h3/a'
author_1_xpath = 'span/a[contains(@href,"author")][1]'
release_date_xpath = './/li[contains(@class, "releaseDateLabel")]/span' 
regex_date_pattern = r"\d{2}-\d{2}-\d{2}"

book_title = []
author_1 = []
release_date = []

for product in products:
    # Extract book title
    title = product.find_elements(By.XPATH, book_title_xpath)
    if title:
        book_title.append(title[0].text)
    
    # Extract first author
    name1 = product.find_elements(By.XPATH, author_1_xpath)
    if name1:
        author_1.append(name1[0].text)

    
    # Extract release date
    book_date = product.find_elements(By.XPATH, release_date_xpath)
    if book_date:
        release_date.append(re.search(regex_date_pattern, book_date[0].text).group())
        

import pandas as pd

print(len(book_title))
print(len(author_1))
print(len(release_date))

# Create a dictionary with the variables
data = {
    'Book_Title' : book_title,
    'Author' : author_1,
    'Release_Date': release_date
}

# Create a dataframe
df = pd.DataFrame(data)

# Export Data as CSV
df.to_csv('audible_aws.csv', index=False)