import time

from selenium import webdriver

# Chrome -> # Chrome Options
# Edge -> Edge Options
# Firefox -> Firefox Options

def test_open_login():
    chrome_options = webdriver.ChromeOptions()
    # Give some extra argument or extension or anything to Chrome.
    # Chrome Options  - Chrome with the Extension, Window Size, Proxy, JS disabled

    extension_path = "/Users/pramod/Downloads/adblocker1x.crx"
    chrome_options.add_extension(extension_path)

    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options) # Fresh chrome which doesn't have anything
    driver.get("https://google.com")

    print(driver.title)
    time.sleep(2000)
