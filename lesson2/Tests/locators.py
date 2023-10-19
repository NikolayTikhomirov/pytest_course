from selenium.webdriver.common.by import By

#AUTH

USERNAME_FIELD = (By.XPATH, "//input[@data-test='username']")
PASSWORD_FIELD = (By.XPATH, "//input[@data-test='password']")
LOGIN_BUTTON = (By.XPATH, "//input[@data-test='login-button']")


# Burger menu
BURGER_MENU = (By.XPATH, "//button[@id='react-burger-menu-btn']")

CREDENTIALS_ERROR_TEXT = "Epic sadface: Username and password do not match any user in this service"