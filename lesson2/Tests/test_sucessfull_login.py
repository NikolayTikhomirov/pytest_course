from time import sleep
from locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON
from global_variables import LOGIN, PASSWORD, MAIN_PAGE, INVENTORY_PAGE, TIMEOUT


def test_login_form(driver):
    driver.get(MAIN_PAGE)

    # вводим валидный логин в поле "Username"
    driver.find_element(*USERNAME_FIELD).send_keys(LOGIN)

    # вводим валидный пароль в поле "Password"
    driver.find_element(*PASSWORD_FIELD).send_keys(PASSWORD)

    # кликаем на кнопку "Login"
    driver.find_element(*LOGIN_BUTTON).click()

    sleep(TIMEOUT)
    assert driver.current_url == INVENTORY_PAGE
