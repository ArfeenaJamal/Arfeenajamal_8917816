from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the webdriver (make sure 'chromedriver' is in your PATH or provide the full path)
driver = webdriver.Chrome()

try:
    # Action 1: Open Wikipedia homepage
    driver.get("https://www.wikipedia.org/")
    time.sleep(10)  # Wait for page to load

    # Action 2: Search for "Selenium"
    search_box = driver.find_element(By.ID, "searchInput")
    search_box.send_keys("Selenium")
    search_box.send_keys(Keys.RETURN)
    time.sleep(10)  # Wait for search results to load

    # Action 3: Return to Wikipedia homepage
    driver.get("https://www.wikipedia.org/")
    time.sleep(10)  # Wait for page to load

    # Action 4: Search for "Meta-Wiki"
    search_box = driver.find_element(By.ID, "searchInput")
    search_box.clear()  # Clear previous search
    search_box.send_keys("Meta-Wiki")
    search_box.send_keys(Keys.RETURN)
    time.sleep(10)  # Wait for search results to load

    # Action 5: Click on a YouTube video link
    youtube_link = driver.find_element(By.PARTIAL_LINK_TEXT, "YouTube")
    youtube_link.click()
    time.sleep(10)  # Wait for YouTube page to load

    print("Test completed successfully.")

finally:
    # Action 6: Back to Wikipedia homepage in the finally block
    driver.get("https://www.wikipedia.org/")
    time.sleep(10)  # Wait for page to load

    # Close the browser
    driver.quit()
