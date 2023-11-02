import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_open_browser(driver):
    locator = (By.ID, 'ui-id-8')
    driver.get("https://magento.softwaretestingboard.com/")
    time.sleep(5)
    element = driver.find_element(*locator)
    element.click()
    driver.back()
    time.sleep(5)
    driver.forward()
    time.sleep(5)
    driver.refresh()
    time.sleep(5)


def test_open_browser1(driver):
    start_time = time.time()
    driver.get("https://magento.softwaretestingboard.com/")
    end_time = time.time()
    print(end_time - start_time)
