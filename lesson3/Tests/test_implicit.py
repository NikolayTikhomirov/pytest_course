import variables as v
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--incognito')
    options.add_argument('--headless')
    return options

@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(v.MAX_TIMEOUT)
    yield driver
    driver.quit()

def test_site_registration(driver):
    driver.get(v.MAIN_PAGE)
    assert driver.find_element(*v.SITE_TITLE).text == v.SITE_TITLE_TEXT,\
        "Site title is not 'Практика с ожиданиями в Selenium'"

    driver.find_element(*v.START_TESTING_BUTTON).click()
    driver.find_element(*v.LOGIN_FIELD).send_keys(v.LOGIN)
    driver.find_element(*v.PASSWORD_FIELD).send_keys(v.PASSWORD)
    driver.find_element(*v.AGREE_CHECKBOX).click()
    driver.find_element(*v.REGISTRATION_BUTTON).click()
    assert driver.find_element(*v.LOADER_INDICATOR).is_displayed(),\
        "Loading indicator is not displayed"

    WebDriverWait(driver, v.MAX_TIMEOUT).until(EC.invisibility_of_element_located(v.LOADER_INDICATOR))
    assert driver.find_element(*v.SUCCESS_MESSAGE).text == v.SUCCESS_MESSAGE_TEXT,\
        "Message 'Вы успешно зарегистрированы' is not displayed"
