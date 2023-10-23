from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
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

def test_successful_login(site_auth):
    assert site_auth.current_url == gv.INVENTORY_PAGE
