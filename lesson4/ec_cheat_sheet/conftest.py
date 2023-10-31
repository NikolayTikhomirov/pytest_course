from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def options():
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--start-maximized')
    # options.add_argument("--incognito")
    return options 


@pytest.fixture 
def driver(options):
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout = 15)
    return wait 
