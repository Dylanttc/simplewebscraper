from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Set up the driver with the path to your chromedriver.exe
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

# Navigate to Google
driver.get("https://www.google.com")

# Find the search box using its name attribute value
search_box = driver.find_element(By.NAME, "q")

# Send a search query to the search box
search_box.send_keys("Hello World")

# Submit the search form
search_box.submit()

# Wait for a few seconds to see the result (this is just for demonstration purposes)
import time
time.sleep(5)

# Close the browser
driver.quit()
