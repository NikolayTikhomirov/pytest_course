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

# Broken images
IMAGES_ELEMENTS = (By.XPATH, "//div[@class='example']/img")
IMAGE_CONTAINER = (By.XPATH, "//div[@class='example']")
IMG_CHILD_ELEMENTS = (By.XPATH, ".//img")

# Checkboxes
CHECKBOX_1 = (By.XPATH, "//input[@type='checkbox'][1]")
CHECKBOX_2 = (By.XPATH, "//input[@type='checkbox'][2]")

# Dynamically Loaded Page Elements (for both pages)
START_BUTTON = (By.XPATH, "//button[text()='Start']")
LOADING_BAR = (By.XPATH, "//div[@id='loading']")
HELLO_WORLD_ELEMENT = (By.XPATH, "//h4[text()='Hello World!']")

# Other elements
ANY_CHILD_ELEMENT = (By.XPATH, "./*")
