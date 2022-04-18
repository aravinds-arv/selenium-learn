from re import U
from turtle import up
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://orteil.dashnet.org/cookieclicker")
driver.implicitly_wait(20)
cookie = driver.find_element(by=By.ID, value="bigCookie")
cookie_count = driver.find_element(by=By.ID, value="cookies")
items = [driver.find_element(by=By.ID, value=f"productPrice{str(i)}") for i in range(1,-1,-1)]

for i in range(5000):
    actions = ActionChains(driver)
    actions.click(cookie)
    actions.perform()
    count = int(cookie_count.text.split()[0])
    for item in items:
        if int(item.text) <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()


