# Selenium ?
# Selenium 3, 4 ?
# Selenium 3 ->  Selenium 4

# Selenium 3
# 1.you need to Setup the Browser Drivers - Machine - PC/Mac
# 2. Problem - browser


# Selenium 4 ( most 70% ) Selenium 4
# W3c - protocol, Selenium Manager - Which will automatically download the
# browser driver for you

# QA -> Focus -> Test case

from selenium import webdriver


def test_open_login():
    driver = webdriver.Chrome()
    # Create a Session with POST Request(API POST Request),
    # Fresh Chrome Browser will be open, Session ID is created. #3l2kjh3g2hj1kl2
    # SessionId - 68614348f0cb4f521b963ed00eefbd0a
    driver.get("https://google.com")
    driver.maximize_window()
    print(driver.title)


    # 1 Session ID -> close ID will be deleted
    # Multiple windows in same session.
