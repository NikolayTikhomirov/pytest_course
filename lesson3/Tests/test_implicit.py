import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Variables
MAX_TIMEOUT = 60
PASSWORD = "password"
LOGIN = "login"
SITE_TITLE_TEXT = "Практика с ожиданиями в Selenium"
SUCCESS_MESSAGE_TEXT = "Вы успешно зарегистрированы!"

# url
MAIN_PAGE = "https://victoretc.github.io/selenium_waits/"

# Locators
SITE_TITLE = (By.XPATH, "//h1")
START_TESTING_BUTTON = (By.XPATH, "//button[text()='Начать тестирование']")
LOGIN_FIELD = (By.XPATH, "//input[@id='login']")
PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
AGREE_CHECKBOX = (By.XPATH, "//input[@id='agree']")
REGISTRATION_BUTTON = (By.XPATH, "//button[@id='register']")
LOADER_INDICATOR = (By.XPATH, "//div[@id='loader']")
SUCCESS_MESSAGE = (By.XPATH, "//p[@id='successMessage']")

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
    driver.implicitly_wait(MAX_TIMEOUT)
    yield driver
    driver.quit()

def test_site_registration(driver):
    driver.get(MAIN_PAGE)
    assert driver.find_element(*SITE_TITLE).text == SITE_TITLE_TEXT,\
        "Site title is not 'Практика с ожиданиями в Selenium'"

    driver.find_element(*START_TESTING_BUTTON).click()
    driver.find_element(*LOGIN_FIELD).send_keys(LOGIN)
    driver.find_element(*PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(*AGREE_CHECKBOX).click()
    driver.find_element(*REGISTRATION_BUTTON).click()
    assert driver.find_element(*LOADER_INDICATOR).is_displayed(),\
        "Loading indicator is not displayed"

    # Waiting for the loading indicator to disappear and a message to appear
    WebDriverWait(driver, MAX_TIMEOUT).until(EC.all_of(
            EC.invisibility_of_element_located(LOADER_INDICATOR),
            EC.presence_of_element_located(SUCCESS_MESSAGE)))
    # Checking for a message
    assert driver.find_element(*SUCCESS_MESSAGE).text == SUCCESS_MESSAGE_TEXT,\
        "Message 'Вы успешно зарегистрированы' is not displayed"
