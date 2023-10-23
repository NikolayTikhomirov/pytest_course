import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import locators as l
import global_variables as gv
from time import sleep

@pytest.fixture
def chrome_options():
    options = Options()
    # options.add_argument('--window-size=100,100')
    options.add_argument('--incognito')
    # options.add_argument('--headless')
    return options

@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    # Implicitly wait by default for all elements
    driver.implicitly_wait(gv.MAX_TIMEOUT)
    yield driver
    driver.quit()

@pytest.fixture
def log_in(driver):
    driver.get(gv.MAIN_PAGE)
    driver.find_element(*l.USERNAME_FIELD).send_keys(gv.LOGIN)
    driver.find_element(*l.PASSWORD_FIELD).send_keys(gv.PASSWORD)
    driver.find_element(*l.LOGIN_BUTTON).click()
    return driver

@pytest.fixture
def log_out(log_in):
    driver = log_in
    driver.find_element(*l.BURGER_MENU).click()
    driver.find_element(*l.LOGOUT).click()
    return driver

@pytest.fixture
def setup_teardown(driver):
    # Pre-condition (setup) - user logged in, shopping cart is empty
    driver.get(gv.MAIN_PAGE)
    driver.find_element(*l.USERNAME_FIELD).send_keys(gv.LOGIN)
    driver.find_element(*l.PASSWORD_FIELD).send_keys(gv.PASSWORD)
    driver.find_element(*l.LOGIN_BUTTON).click()
    driver.find_element(*l.BURGER_MENU).click()
    driver.find_element(*l.RESET_APP_STATE).click()
    driver.find_element(*l.CLOSE_BUTTON).click()
    yield driver # Test run
    # Post-condition (teardown) - cart is empty, shopping user logged out
    driver.find_element(*l.BURGER_MENU).click()
    driver.find_element(*l.RESET_APP_STATE).click()
    driver.find_element(*l.LOGOUT).click()
