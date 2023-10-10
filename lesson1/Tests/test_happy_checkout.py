from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker

driver = webdriver.Chrome()

def test_login_form():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(1)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

def test_add_item_to_cart():
    bike_light_add_to_cart = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
    bike_light_add_to_cart.click()

    time.sleep(1)
    shopping_cart_badge = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
    assert shopping_cart_badge.text == "1"

def test_go_to_cart():
    shopping_cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    shopping_cart.click()

    time.sleep(1)
    assert driver.current_url == "https://www.saucedemo.com/cart.html"

    bike_light_title = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
    assert bike_light_title.text == "Sauce Labs Bike Light"

def test_checkout():
    checkout_button = driver.find_element(By.XPATH, "//button[@id='checkout']")
    checkout_button.click()

    time.sleep(1)
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"

    fake = Faker()
    first_name_field = driver.find_element(By.XPATH, "//input[@id='first-name']")
    first_name_field.send_keys(fake.first_name())

    last_name_field = driver.find_element(By.XPATH, "//input[@id='last-name']")
    last_name_field.send_keys(fake.last_name())

    zip_code_field = driver.find_element(By.XPATH, "//input[@id='postal-code']")
    zip_code_field.send_keys(fake.postcode())

    continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
    continue_button.click()

    time.sleep(1)
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"

    cart_item_title = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")
    assert cart_item_title.text == "Sauce Labs Bike Light"

    finish_button = driver.find_element(By.XPATH, "//button[@id='finish']")
    finish_button.click()

    time.sleep(1)
    assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html"

def test_logout_link():

    burger_menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
    burger_menu.click()

    time.sleep(1)
    logout_link = driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']")
    logout_link.click()

    time.sleep(1)
    assert driver.current_url == "https://www.saucedemo.com/"

    driver.quit()
