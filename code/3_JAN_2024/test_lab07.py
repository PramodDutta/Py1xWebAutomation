import time

from selenium import webdriver


# Chrome -> # Chrome Options
# Edge -> Edge Options
# Firefox -> Firefox Options

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")

    # <input - Open Tag
    # type="email"
    # class="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # > Close Tag










    time.sleep(5)
    # driver.close()
    driver.quit()
