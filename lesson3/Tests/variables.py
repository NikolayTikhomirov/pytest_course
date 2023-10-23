from selenium.webdriver.common.by import By

# Variables
TIMEOUT = 10
MAX_TIMEOUT = 60
PASSWORD = "password"
LOGIN = "login"
SITE_TITLE_TEXT = "Практика с ожиданиями в Selenium"
SUCCESS_MESSAGE_TEXT = "Вы успешно зарегистрированы!"

# url
MAIN_PAGE = "https://victoretc.github.io/selenium_waits/"

# Locators
SITE_TITLE = (By.XPATH, "//h1")
START_TESTING_BUTTON = (By.XPATH, "//button[text()='Начать тестирование']")
LOGIN_FIELD = (By.XPATH, "//input[@id='login']")
PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
AGREE_CHECKBOX = (By.XPATH, "//input[@id='agree']")
REGISTRATION_BUTTON = (By.XPATH, "//button[@id='register']")
LOADER_INDICATOR = (By.XPATH, "//div[@id='loader']")
SUCCESS_MESSAGE = (By.XPATH, "//p[@id='successMessage']")
