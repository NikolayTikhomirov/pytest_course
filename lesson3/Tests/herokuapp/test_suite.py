import locators as L
import global_variables as GV
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def test_add_2_remove_1_element(driver):
    # All delete buttons the same and located in 1 div element
    def number_of_del_buttons():
        container = driver.find_element(*L.DELETE_BUTTONS_CONTAINER)
        num_of_del_buttons = len(container.find_elements(*L.ANY_CHILD_ELEMENT))
        return num_of_del_buttons

    driver.get(GV.ADD_REMOVE_ELEMENTS_PAGE)
    assert driver.current_url == GV.ADD_REMOVE_ELEMENTS_PAGE

    assert number_of_del_buttons() == 0

    driver.find_element(*L.ADD_ELEMENT_BUTTON).click()
    assert number_of_del_buttons() == 1

    driver.find_element(*L.ADD_ELEMENT_BUTTON).click()
    assert number_of_del_buttons() == 2

    driver.find_element(*L.DELETE_ELEMENT_BUTTON).click()
    assert number_of_del_buttons() == 1

def test_basic_auth(driver):
    pass

def test_broken_images(driver):
    pass

def test_checkbox(driver):
    pass