import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Chrome -> # Chrome Options
# Edge -> Edge Options
# Firefox -> Firefox Options

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    mp_btn = driver.find_element(By.ID, "btn-make-appointment")
    mp_btn.click()

    print(driver.current_url)
    # Verification of the URL
    # assert
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", "Error wrong URL"

    username = driver.find_element(By.NAME,"username")
    username.send_keys("John Doe")

    password = driver.find_element(By.ID, "txt-password")

    password.send_keys("ThisIsNotAPassword")

    submit_btn = driver.find_element(By.ID, "btn-login")
    submit_btn.click()


    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", "Error wrong URL"


    # Custom attribute it is not id, name, class -> Custom Attribute -
    # student = "praveen" , roll=123, phone="233", placeholder="dasda"
    #data-qa="dasda" , testID="123"

    # <input
    # type="password"
    # class="form-control"
    # placeholder="Password"
    # student="praveen"
    # value=""
    # autocomplete="off">





    time.sleep(5)
    # driver.close()
    driver.quit()
