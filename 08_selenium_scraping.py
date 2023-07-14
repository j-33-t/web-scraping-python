from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Safari()

url = "https://www.adamchoi.co.uk/overs/detailed"
driver.get(url)


# Find the element using xpath
all_matches_button = driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/home-away-selector/div/div/div/div/label[2]')
all_matches_button.click()

matches = driver.find_elements(By.TAG_NAME, 'tr')

date = []
home_team = []
score = []
away_team = []

# X Path indexing starts with 1, Unlike python's 0 
for i in range(5):
    date.append(matches[i].find_element(By.XPATH, './td[1]').text)
    home_team.append((matches[i].find_element(By.XPATH, './td[2]').text))
    score.append((matches[i].find_element(By.XPATH, './td[3]').text))
    away_team.append((matches[i].find_element(By.XPATH, './td[4]').text))

    # Printing for checking process and debugging
    print(home_team[i])


import pandas as pd

# Create a dictionary with the variables
data = {
    'Date': date,
    'Home Team': home_team,
    'Score': score,
    'Away Team': away_team
}

# Create a dataframe
df = pd.DataFrame(data)

# Export Data as CSV
df.to_csv('england_football_matches.csv', index=False)





