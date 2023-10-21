import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON
from global_variables import LOGIN, PASSWORD, MAIN_PAGE, INVENTORY_PAGE, MAX_TIMEOUT

@pytest.fixture
def chrome_options():
    options = Options()
    # options.add_argument('--window-size=100,100')
    options.add_argument('--incognito')
    # options.add_argument('--headless')
    return options

@pytest.fixture()
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(MAX_TIMEOUT)
    yield driver
    driver.quit()

@pytest.fixture()
def site_auth(driver):
    driver.get(MAIN_PAGE)
    driver.find_element(*USERNAME_FIELD).send_keys(LOGIN)
    driver.find_element(*PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()
