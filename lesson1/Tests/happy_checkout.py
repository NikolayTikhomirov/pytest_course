from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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

def test_logout_link():

    burger_menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
    burger_menu.click()

    time.sleep(1)
    logout_link = driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']")
    logout_link.click()

    time.sleep(1)
    assert driver.current_url == "https://www.saucedemo.com/"

    driver.quit()










