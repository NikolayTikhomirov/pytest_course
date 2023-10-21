from locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON
from global_variables import LOGIN, PASSWORD, MAIN_PAGE, INVENTORY_PAGE

def test_login_form(driver):
    driver.get(MAIN_PAGE)
    driver.find_element(*USERNAME_FIELD).send_keys(LOGIN)
    driver.find_element(*PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()
    assert driver.current_url == INVENTORY_PAGE
