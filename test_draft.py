from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker

TIMEOUT = 0.01
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
    onesie_link_name = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Onesie']")
    onesie_link_name.click()
    time.sleep(TIMEOUT)

    onesie_add_to_cart = driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-onesie']")
    onesie_add_to_cart.click()
    time.sleep(TIMEOUT)
    shopping_cart_badge = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
    assert shopping_cart_badge.text == "1"
    time.sleep(TIMEOUT)

    onesie_remove_from_cart = driver.find_element(By.XPATH, "//button[@data-test='remove-sauce-labs-onesie']")
    onesie_remove_from_cart.click()
    time.sleep(TIMEOUT)

    shopping_cart_badge = driver.find_elements(By.XPATH, "//span[@class='shopping_cart_badge']")
    assert len(shopping_cart_badge) == 0

    driver.quit()
