from selenium.webdriver.common.by import By

# Authorization
USERNAME_FIELD = (By.XPATH, "//input[@data-test='username']")
PASSWORD_FIELD = (By.XPATH, "//input[@data-test='password']")
LOGIN_BUTTON = (By.XPATH, "//input[@data-test='login-button']")
LOGIN_ERROR = (By.XPATH, "//div[@class='error-message-container error']")



# Add/Remove Elements
ADD_ELEMENT_BUTTON = (By.XPATH, "//button[text()='Add Element']")
DELETE_ELEMENT_BUTTON = (By.XPATH, "//div[@id='elements']/button")
DELETE_BUTTONS_CONTAINER = (By.XPATH, "//div[@id='elements']")

# Basic auth
AUTH_MESSAGE = (By.XPATH, "//p")

# Other elements
ANY_CHILD_ELEMENT = (By.XPATH, "./*")
