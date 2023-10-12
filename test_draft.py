from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker

TIMEOUT = 1
driver = webdriver.Chrome()

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

