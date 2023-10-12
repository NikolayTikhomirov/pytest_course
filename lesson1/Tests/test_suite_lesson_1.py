from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker

TIMEOUT = 0.1
CREDENTIALS_ERROR_TEXT = "Epic sadface: Username and password do not match any user in this service"
driver = webdriver.Chrome()


def test_login_form_error():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("user")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(TIMEOUT)
    assert driver.current_url == "https://www.saucedemo.com/"

def test_login_form():

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.clear()
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.clear()
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(TIMEOUT)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

def test_about_link():

    burger_menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
    burger_menu.click()

    time.sleep(TIMEOUT)
    about_link = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
    about_link.click()

    time.sleep(TIMEOUT)
    assert driver.current_url == "https://saucelabs.com/"
    driver.back()
    time.sleep(TIMEOUT)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

def test_add_catalog_item_to_cart():
    bike_light_add_to_cart = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
    bike_light_add_to_cart.click()
    time.sleep(TIMEOUT)
    shopping_cart_badge = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
    assert shopping_cart_badge.text == "1"

def test_from_catalog_to_card_via_picture():
    red_tshirt_img = driver.find_element(By.XPATH, "//a[@id='item_3_img_link']")
    red_tshirt_img.click()
    time.sleep(TIMEOUT)
    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=3"

def test_add_card_item_to_cart():
    red_tshirt_add_to_cart = driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
    red_tshirt_add_to_cart.click()
    time.sleep(TIMEOUT)
    shopping_cart_badge = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
    assert shopping_cart_badge.text == "2"

def test_go_to_cart():
    shopping_cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    shopping_cart.click()

    time.sleep(TIMEOUT)
    assert driver.current_url == "https://www.saucedemo.com/cart.html"

    bike_light_title = driver.find_element(By.XPATH, "//a[@id='item_0_title_link']")
    assert bike_light_title.text == "Sauce Labs Bike Light"

def test_delete_item_from_cart():
    red_tshirt_remove = driver.find_element(By.XPATH, "//button[@id='remove-test.allthethings()-t-shirt-(red)']")
    red_tshirt_remove.click()
    time.sleep(TIMEOUT)
    shopping_cart_badge = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
    assert shopping_cart_badge.text == "1"

def test_checkout():
    checkout_button = driver.find_element(By.XPATH, "//button[@id='checkout']")
    checkout_button.click()

    time.sleep(TIMEOUT)
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

    time.sleep(TIMEOUT)
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"

    cart_item_title = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")
    assert cart_item_title.text == "Sauce Labs Bike Light"

    finish_button = driver.find_element(By.XPATH, "//button[@id='finish']")
    finish_button.click()

    time.sleep(TIMEOUT)
    assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html"

def test_all_items_link():
    burger_menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
    burger_menu.click()

    time.sleep(TIMEOUT)
    all_items = driver.find_element(By.XPATH, "//a[@id='inventory_sidebar_link']")
    all_items.click()

    time.sleep(TIMEOUT)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

def test_name_za_filter():
    name_desc_filter = driver.find_element(By.XPATH, '//option[@value="za"]')
    name_desc_filter.click()
    first_item = driver.find_element(By.XPATH, '//div[@class="inventory_item"][1]')
    first_item_name = first_item.text.splitlines()[0]
    time.sleep(TIMEOUT)
    assert first_item_name == "Test.allTheThings() T-Shirt (Red)"

def test_price_lohi_filter():
    price_asc_filter = driver.find_element(By.XPATH, '//option[@value="lohi"]')
    price_asc_filter.click()
    first_item = driver.find_element(By.XPATH, '//div[@class="inventory_item"][1]')
    first_item_name = first_item.text.splitlines()[2]
    time.sleep(TIMEOUT)
    assert first_item_name == "$7.99"

def test_price_hilo_filter():
    price_desc_filter = driver.find_element(By.XPATH, '//option[@value="hilo"]')
    price_desc_filter.click()
    first_item = driver.find_element(By.XPATH, '//div[@class="inventory_item"][1]')
    first_item_name = first_item.text.splitlines()[2]
    time.sleep(TIMEOUT)
    assert first_item_name == "$49.99"

def test_price_az_filter():
    name_asc_filter = driver.find_element(By.XPATH, '//option[@value="az"]')
    name_asc_filter.click()
    first_item = driver.find_element(By.XPATH, '//div[@class="inventory_item"][1]')
    first_item_name = first_item.text.splitlines()[0]
    time.sleep(TIMEOUT)
    assert first_item_name == "Sauce Labs Backpack"

def test_logout_link():

    burger_menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
    burger_menu.click()

    time.sleep(TIMEOUT)
    logout_link = driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']")
    logout_link.click()

    time.sleep(TIMEOUT)
    assert driver.current_url == "https://www.saucedemo.com/"

    driver.quit()
