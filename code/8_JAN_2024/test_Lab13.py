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

    # //tagName[@attribute=value]
    # SelectorsHub.com - Xpath
    # make_appointment_btn = driver.find_element(By.XPATH,"//a[@id='btn-make-appointment']")
    # make_appointment_btn_text = driver.find_element(By.XPATH,"//a[text()='Make Appointment']")
    make_appointment_btn_partial = driver.find_element(By.XPATH, "//a[contains(text(),'Make App')]")

    # //a[text()="Make Appointment" and contains(@id,"btn-make-appointment")]




    make_appointment_btn_partial.click()

    # Make Appointment Button

    # //a[@id='btn-make-appointment'] - Relative Direct

    # //*[@id='btn-make-appointment'] - This is called * wild card ,
    # Find id = btn-make-app in All the TagNames, this will be a Slow xpath

    # XPATH Functions

    # Full Visible Text Match
    # Text() -> //a[text()='Make Appointment']

    # Partial Match

    # Contains
    # // a[contains(text(), 'Make App')]
    # // a[contains(text(), 'Make')]

    list_elements_p = driver.find_elements(By.XPATH, "//p[contains(text(),'A')]")
    for i in list_elements_p:
        if i.text == "Copyright © CURA Healthcare Service 2024":
            i.click()
        print(i.text)

    # Start-with
    # //a[starts-with(text(),'Make')]
    # End-With

    # Abs - Not recommended - Never use it
    # /html/body/header/div/a
    # Start from the Root

    # Xpath?  Relative or Abs?

    # Find the p tag via the contains functions
    # //p[contains(text(),'Copyright')]
    # //p[contains(@class,'muted')]


    # Xpath OR and And
    # //p[contains(text(),'A') and contains(@class,"mute")] - Single element
    # //p[contains(text(),'A') or contains(@class,"mute")]


    ptag = driver.find_element(By.CLASS_NAME, "text-muted")
    print(ptag.text)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"





    time.sleep(5)
    driver.quit()
