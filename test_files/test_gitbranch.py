from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver (Chrome)
driver = webdriver.Chrome()

try:
    # Step 1: Open Google
    driver.get("https://www.google.com")
    time.sleep(2)

    # Step 2: Find the search box and enter a query
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium with Python")
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    # Step 3: Validate results
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    assert len(results) > 0, "No search results found!"

    print("Test Passed: Search results displayed successfully.")

except Exception as e:
    print("Test Failed:", e)

finally:
    # Close browser
    driver.quit()
