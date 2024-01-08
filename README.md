## Py1x Web Automation Repo

## Install the Import Lib
- Selenium ( > 4))
- Pytest
- Allure Pytest
- Pytest HTML
- xdist - Run Parallel Execution
- logging - Logging (API lib)
- Openpyxl - CSV,Excel
- Faker lib( Fake data generation)**

``pip install selenium pytest pytest-html allure-pytest
``


## How to Push the Git
1. git add .
2. git commit -m "Message"
3. git push 
4. git pull ( if You have added somehting on Github.com)



# How to run your Testcase Parallelly 
```pip install pytest-xdist```
```pytest -n auto code/8_JAN_2024/test_Lab14.py -s -v```