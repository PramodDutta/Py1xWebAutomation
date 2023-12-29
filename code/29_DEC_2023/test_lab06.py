import time

from selenium import webdriver


# Chrome -> # Chrome Options
# Edge -> Edge Options
# Firefox -> Firefox Options

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    # driver.navigate().to x
    print(driver.title)


    # Navigation Command
    driver.back()
    driver.get("https://www.bing.com")
    print(driver.title)

    driver.forward()
    print(driver.title)

    driver.back()
    print(driver.title)
    driver.refresh()

    time.sleep(5)
    driver.quit()
