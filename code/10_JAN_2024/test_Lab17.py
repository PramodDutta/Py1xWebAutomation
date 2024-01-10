import os
import time

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException)


# XPath Functions
# XPath Axes
# CSS Selectors
# Alerts

@pytest.mark.positive
# pytest -k "positive" *
def test_vwologin_positve():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    # driver.implicitly_wait(20)
    #
    # # e1, e2 ???
    # # # Tell Webdriver to wait for 20 Seconds to Load - All the elements
    # # # What if e1,e2,e3 <  20 waste of time

    # CSS Selector - Try to use all the CSS in the script

    email_input = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    pass_input = driver.find_element(By.CSS_SELECTOR, "[name='password']")
    submit_input = driver.find_element(By.CSS_SELECTOR, "button[id='js-login-btn']")

    email_input.send_keys(os.getenv("EMAIL"))
    pass_input.send_keys(os.getenv("PASSWORD"))

    submit_input.click()

    # time.sleep(15) #-> Thread.sleep() , JVM will wait.
    # Add a condition so that Webdriver should wait for that condition

    # pageTitle  - Click ->

    # WebDriverWait(driver, 15).until(
    #     # EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".page-heading"), "Dashboard")
    #     # EC.url_contains("dashboard")
    #     #EC.visibility_of(By.CSS_SELECTOR,".page-heading")
    # )
    # e1 -> 1,2,3,4,5(mini seconds), 6.3ms -> continously checking ->  7th we are find it, move next command.

    # WebDriverWait(driver, 15).until(
    #     EC.text_to_be_present_in_element((By.XPATH, "//span[@data-qa='lufexuloga']"), "Aman")
    # )


    # Fluent Wait -> Condition + Frequency, -> Customize Exception
    #  e1 -> page heading -> 1,2,3,4,5 -> 6.3 ms -> move to next command
    # e1 -> Frequency - 1, check after 1 element visible? , 2, 3 4 , 5 , 6, 7 -> Move Next



    ignore_list =[ElementNotVisibleException, ElementNotSelectableException]
    wait = WebDriverWait(driver,15, poll_frequency=1, ignored_exceptions=ignore_list)
    element = EC.presence_of_element_located((By.CSS_SELECTOR,".page-heading"))
    # PF = 1  EF = NO, t < 15 , WD - Should Exception ?
    # PF = 2  EF = NO, m < 10 , WD - Should Exception ?
    # ......
    # PF = 15  EF = NO, m = 15 , WD - Should Exception Yes





    heading_element = driver.find_element(By.XPATH, "//span[@data-qa='lufexuloga']");
    assert heading_element.text == os.getenv("USERNAME")

    time.sleep(5)
    driver.quit()
