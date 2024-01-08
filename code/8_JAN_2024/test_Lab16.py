import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# XPath Functions
# XPath Axes
# CSS Selectors
# Alerts

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")

    email_input = driver.find_element(By.XPATH, "//p[@class='page-sub-title']")
    pass_input = driver.find_element(By.CSS_SELECTOR, "[name='password']")
    submit_input = driver.find_element(By.CSS_SELECTOR, "button[id='js-login-btn']")

    email_input.send_keys("admin")
    pass_input.send_keys("admin")

    submit_input.click()







    time.sleep(5)
    driver.quit()