import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# XPath Functions
# XPath Axes
# CSS Selectors
# Alerts

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    assert driver.title == "CURA Healthcare Service"

    make_appointment_btn_partial = driver.find_element(By.XPATH, "//a[contains(text(),'Make App')]")
    make_appointment_btn_partial.click()


    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(5)
    driver.quit()

    # I am also and start in plateform?

def test_open_login_Edge():
    driver = webdriver.Edge()
    #driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    assert driver.title == "CURA Healthcare Service"

    make_appointment_btn_partial = driver.find_element(By.XPATH, "//a[contains(text(),'Make App')]")
    make_appointment_btn_partial.click()


    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(5)
    driver.quit()