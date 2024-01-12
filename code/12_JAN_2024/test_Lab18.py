import os
import time
import openpyxl
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException)


def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({"username": username, "password": password})
    return credentials

@pytest.mark.positive
def test_vwologin_positve():
    file_path = os.getcwd()
    full_file_path = file_path+"/testdata_ddt.xlsx"
    credentials = read_credentials_from_excel(full_file_path)

    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username,password)
        vwo_login(username,password)






def vwo_login(username,password):
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    email_input = driver.find_element(By.CSS_SELECTOR, "[name='username']")
    pass_input = driver.find_element(By.CSS_SELECTOR, "[name='password']")
    submit_input = driver.find_element(By.CSS_SELECTOR, "button[id='js-login-btn']")

    email_input.send_keys(username)
    pass_input.send_keys(password)

    submit_input.click()
    # Write the loginc if test case pass
    # -> URL changes
    # -> Error Message
    driver.quit()
