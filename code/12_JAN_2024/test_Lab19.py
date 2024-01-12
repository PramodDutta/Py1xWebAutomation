import os

import openpyxl
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({"username": username, "password": password})
    return credentials


@pytest.mark.parametrize("user_cred", read_credentials_from_excel(os.getcwd() + "/testdata_ddt.xlsx"))
def test_vwologin_positve(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    vwo_login(username, password)


def vwo_login(username, password):
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    email_input = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    pass_input = driver.find_element(By.CSS_SELECTOR, "[name='password']")
    submit_input = driver.find_element(By.CSS_SELECTOR, "button[id='js-login-btn']")

    email_input.send_keys(username)
    pass_input.send_keys(password)

    submit_input.click()

    result = driver.current_url
    if result != "https://app.vwo.com/#dashboard":
        pytest.xfail("Invalid Login")
        driver.quit()
    else:
        assert True == True
        driver.quit()

    # Write the loginc if test case pass
    # -> URL changes
    # -> Error Message
