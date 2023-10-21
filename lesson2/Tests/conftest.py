import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
