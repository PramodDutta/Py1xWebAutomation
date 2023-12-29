import time

from selenium import webdriver

# Chrome -> # Chrome Options
# Edge -> Edge Options
# Firefox -> Firefox Options

def test_open_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://google.com")
    print(driver.title)
    # time.sleep(2000)

    # Good practice to use this.

    # Quit the browser and close all the windows,
    # Session id = null
    driver.quit()