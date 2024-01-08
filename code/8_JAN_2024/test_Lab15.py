import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# XPath Functions
# XPath Axes
# CSS Selectors
# Alerts

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")

    assert driver.current_url == "https://www.ebay.com/"

    search_box = driver.find_element(By.XPATH, "//input[@id='gh-ac']")

    search_box.send_keys("16 gb")

    search_btn = driver.find_element(By.XPATH, "//input[@id='gh-btn']")
    search_btn.click()

    list_results = driver.find_elements(By.XPATH,"//span[@role='heading']")
    for i in list_results:
        print(i.text)

    time.sleep(5) # in Future we will remove this



    time.sleep(5)
    driver.quit()