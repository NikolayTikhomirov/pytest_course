from selenium.webdriver.common.by import By

# Authorization
USERNAME_FIELD = (By.XPATH, "//input[@data-test='username']")
PASSWORD_FIELD = (By.XPATH, "//input[@data-test='password']")
LOGIN_BUTTON = (By.XPATH, "//input[@data-test='login-button']")
LOGIN_ERROR = (By.XPATH, "//div[@class='error-message-container error']")

# Burger menu
BURGER_MENU = (By.XPATH, "//button[@id='react-burger-menu-btn']")
CLOSE_BUTTON = (By.XPATH, "//button[@id='react-burger-cross-btn']")
ALL_ITEMS = (By.XPATH, "//a[@id='inventory_sidebar_link']")
ABOUT = (By.XPATH, "//a[@id='about_sidebar_link']")
LOGOUT = (By.XPATH, "//a[@id='logout_sidebar_link']")
RESET_APP_STATE = (By.XPATH, "//a[@id='reset_sidebar_link']")

# Inventory
ADD_TO_CART_FIRST_INVENTORY_ITEM = (By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory ']")

# Prodict filters
NAME_AZ_FILTER = (By.XPATH, "//option[@value='az']")
NAME_ZA_FILTER = (By.XPATH, "//option[@value='za']")
PRICE_LH_FILTER = (By.XPATH, "//option[@value='lohi']")
PRICE_HL_FILTER = (By.XPATH, "//option[@value='hilo']")

# Shopping cart
SHOPPING_CART = (By.XPATH, "//a[@class='shopping_cart_link']")
SHOPPING_CART_BADGE = (By.XPATH, "//span[@class='shopping_cart_badge']")
CHECKOUT_BUTTON = (By.XPATH, "//button[@id='checkout']")

# Checkout
FIRST_NAME = (By.XPATH, "//input[@id='first-name']")
LAST_NAME = (By.XPATH, "//input[@id='last-name']")
ZIP_CODE = (By.XPATH, "//input[@id='postal-code']")
CONTINUE_BUTTON = (By.XPATH, "//input[@id='continue']")
FINISH_BUTTON = (By.XPATH, "//button[@id='finish']")
