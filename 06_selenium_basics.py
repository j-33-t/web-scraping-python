from selenium import webdriver

driver = webdriver.Safari()
  # Add any desired Chrome options here

url = "https://www.adamchoi.co.uk/overs/detailed"
driver.get(url)
