import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://en.wikipedia.org')
time.sleep(3)
search = driver.find_element(by=By.ID, value="searchInput")
search.send_keys("Python")
time.sleep(2)
search.send_keys(Keys.ARROW_DOWN)
search.send_keys(Keys.RETURN)
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "mw-parser-output"))
    )
    headers = main.find_elements(by=By.TAG_NAME, value='h2')
    for header in headers:
        print(header.text[:-6])
finally:
    driver.quit()