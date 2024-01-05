import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Chrome -> # Chrome Options
# Edge -> Edge Options
# Firefox -> Firefox Options

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    # Relative Xpath
    rel_xpath_email = driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']")
    rel_xpath_email.send_keys("augtest_040823@idrive.com")

    time.sleep(5)
    # driver.close()
    driver.quit()
