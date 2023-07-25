from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


import time
import re
import pandas as pd
from datetime import datetime

options = Options()
# options.add_argument('--headless')
options.add_argument('window-size=1920x1080')
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# ------- POINT TO BE NOTED ------------ #
# Defining Explicit Wait time instead of implicit can improve performance 
# ---------------------------------------#


# Instantiate the Chrome driver with the specified options
driver = webdriver.Chrome(options=options)

# ---- URL ----- #
driver.get('https://www.youtube.com/')

time.sleep(3)
# ----- Click Button ----- # 

cookie_consent = driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[1]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')
cookie_consent.click()
time.sleep(3)
# Button change region 

nav_button = driver.find_element(By.XPATH,'//yt-icon[@class = "style-scope ytd-topbar-menu-button-renderer"]')
nav_button.click()
time.sleep(1)


# Region Button
region_button = driver.find_element(By.XPATH,'//div[@class="menu-container style-scope ytd-multi-page-menu-renderer"]//yt-multi-page-menu-section-renderer[2]/div[2]/ytd-compact-link-renderer[3]')
region_button.click() 
time.sleep(1)

# United States
usa_button = driver.find_element(By.XPATH,'//*[@id="items"]/ytd-compact-link-renderer[104]')
usa_button.click() 
time.sleep(5)

# Click nav again
nav_button = driver.find_element(By.XPATH,'//yt-icon[@class = "style-scope ytd-topbar-menu-button-renderer"]')
nav_button.click()
time.sleep(3)

# Language Button
language_button = driver.find_element(By.XPATH,'//div[@class="menu-container style-scope ytd-multi-page-menu-renderer"]//yt-multi-page-menu-section-renderer[2]/div[2]/ytd-compact-link-renderer[1]')
language_button.click()
time.sleep(1)

# English USA
english_usa_button = driver.find_element(By.XPATH,'//*[@id="items"]/ytd-compact-link-renderer[13]')
english_usa_button.click()
time.sleep(3)


# ------ SCROLLING ----------- #

# Define a function to scroll to the bottom of the page
def scroll_to_bottom():
    while True:
        # Get the current height of the page
        current_height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")

        # Scroll to the bottom of the page
        driver.execute_script(f"window.scrollTo(0, {current_height});")

        # Wait for the new content to load (adjust the waiting time as needed)
        WebDriverWait(driver, 10).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
        time.sleep(5)
        # Check if we have reached the bottom of the page
        new_height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
        if new_height == current_height:
            break

# Call the function to scroll to the bottom of the page
scroll_to_bottom()

time.sleep(3)

# -------- ELEMENTS ----------- #

# Main Path
video_row_path = '//ytd-rich-grid-row[@class= "style-scope ytd-rich-grid-renderer"]//div[@id = "details"]'

# Video Title
video_title_path = './/a[contains(@id,"video-title-link")]/yt-formatted-string'

# channel name
channel_name_path = './/div[contains(@class,"ytd-channel-name")]/div/yt-formatted-string/a'

# Excluding shorts 
views_path = './/*[@id="metadata-line"]/span[1]'

# Uploaded Time - Path cannot handle live streams
# uploaded_time = './/*[@id="metadata-line"]/span[2]'

# Extraction timestamp
extraction_timestamp_var = datetime.now().strftime("%Y-%m-%d %H:%M:%S")



# ---- Extraction ------- #
video_title = []
channel = []
video_views = []
extraction_timestamp = []


videos = driver.find_elements(By.XPATH,video_row_path)
counter = 0
for video in videos:
    video_title.append(video.find_element(By.XPATH,video_title_path).text)
    channel.append(video.find_element(By.XPATH,channel_name_path).text)
    video_views.append(video.find_element(By.XPATH,views_path).text)
    extraction_timestamp.append(extraction_timestamp_var)

print(len(video_title))
print(len(channel))
print(len(video_views))
print(len(extraction_timestamp))

# Create a dictionary with the variables
data = {
    'Video_Title' : video_title,
    'Channel_Name' : channel,
    'Views': video_views,
    'Extraction_Timestamp':extraction_timestamp
}

# Create a dataframe
df = pd.DataFrame(data)

# Export Data as CSV
df.to_csv('youtube_homepage_videos.csv', index=False)