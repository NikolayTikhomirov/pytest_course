import variables as v
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--incognito')
    # options.add_argument('--headless')
    return options

@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_site_registration(driver):
    driver.get(v.MAIN_PAGE)
    assert driver.find_element(*v.SITE_TITLE).text == v.SITE_TITLE_TEXT,\
        "Site title is not 'Практика с ожиданиями в Selenium'"
    sleep(v.TIMEOUT)
    driver.find_element(*v.START_TESTING_BUTTON).click()
    driver.find_element(*v.LOGIN_FIELD).send_keys(v.LOGIN)
    driver.find_element(*v.PASSWORD_FIELD).send_keys(v.PASSWORD)
    driver.find_element(*v.AGREE_CHECKBOX).click()
    driver.find_element(*v.REGISTRATION_BUTTON).click()
    assert driver.find_element(*v.LOADER_INDICATOR).is_displayed(),\
        "Loading indicator is not displayed"
    sleep(v.TIMEOUT)
    # Checking for a message
    assert driver.find_element(*v.SUCCESS_MESSAGE).text == v.SUCCESS_MESSAGE_TEXT,\
        "Message 'Вы успешно зарегистрированы' is not displayed"
