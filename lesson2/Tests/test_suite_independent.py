from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from faker import Faker
import locators as l
import global_variables as gv

def test_unsuccessful_login(driver):
    driver.get(gv.MAIN_PAGE)
    driver.find_element(*l.USERNAME_FIELD).send_keys(gv.WRONG_LOGIN)
    driver.find_element(*l.PASSWORD_FIELD).send_keys(gv.WRONG_PASSWORD)
    driver.find_element(*l.LOGIN_BUTTON).click()
    assert driver.current_url == gv.MAIN_PAGE
    # To add a custom error message in this case need to use this construction because
    try: # this expression will return TimeoutException if element l.LOGIN_ERROR is not visible (not False!)
        WebDriverWait(driver, gv.MAX_TIMEOUT).until(EC.visibility_of_element_located(l.LOGIN_ERROR))
    except TimeoutException:
        assert False, "Error message is not visible"

def test_successful_login(log_in):
    assert log_in.current_url == gv.INVENTORY_PAGE

def test_logout(log_out):
    assert log_out.current_url == gv.MAIN_PAGE

def test_happy_path(setup_teardown):
    driver = setup_teardown
    driver.find_element(*l.ADD_TO_CART_FIRST_INVENTORY_ITEM).click()
    assert driver.find_element(*l.SHOPPING_CART_BADGE).text == "1"

    driver.find_element(*l.SHOPPING_CART).click()
    assert driver.current_url == gv.CART_PAGE

    driver.find_element(*l.CHECKOUT_BUTTON).click()
    assert driver.current_url == gv.CHECKOUT_STEP_1

    fake = Faker()
    driver.find_element(*l.FIRST_NAME).send_keys(fake.first_name())
    driver.find_element(*l.LAST_NAME).send_keys(fake.last_name())
    driver.find_element(*l.ZIP_CODE).send_keys(fake.postcode())
    driver.find_element(*l.CONTINUE_BUTTON).click()
    assert driver.current_url == gv.CHECKOUT_STEP_2

    driver.find_element(*l.FINISH_BUTTON).click()
    assert driver.current_url == gv.CHECKOUT_COMPLETE
