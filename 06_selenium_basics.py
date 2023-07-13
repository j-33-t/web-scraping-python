from selenium import webdriver

driver = webdriver.Safari()
  # Add any desired Chrome options here , Chrome didn't work on mac properly hence using Safari

url = "https://www.adamchoi.co.uk/overs/detailed"
driver.get(url)
