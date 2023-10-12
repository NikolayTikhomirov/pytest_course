from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker

TIMEOUT = 0.01
driver = webdriver.Chrome()
# first_item = driver.find_element(By.XPATH, '//div[@class="inventory_item"][1]')

def test_draft():
    # Precondition, "https://www.saucedemo.com/inventory.html" page
    driver.get("https://www.saucedemo.com/")
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")
    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    time.sleep(TIMEOUT)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    # Draft for test scenarios

    # Filters
    name_desc_filter = driver.find_element(By.XPATH, '//option[@value="za"]')
    name_desc_filter.click()
    first_item = driver.find_element(By.XPATH, '//div[@class="inventory_item"][1]')
    first_item_name = first_item.text.splitlines()[2]
    print(first_item_name)

    assert first_item_name == "Test.allTheThings() T-Shirt (Red)"
    driver.quit()
