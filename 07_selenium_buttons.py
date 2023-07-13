from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Safari()

url = "https://www.adamchoi.co.uk/overs/detailed"
driver.get(url)

time.sleep(2)

# Find the element using xpath
all_matches_button = driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]')
all_matches_button.click()

time.sleep(2)
