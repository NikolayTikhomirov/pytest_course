import time

from selenium.webdriver.common.by import By

YES_BUTTON = (By.CSS_SELECTOR, "label[for='yesRadio']")
IMPRESSIVE_BUTTON = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
NO_BUTTON = (By.CSS_SELECTOR, "label[for='noRadio']")
TEXT_YES = (By.CSS_SELECTOR, "span[class='text-success']")


def test_check_radio_button(driver):
    driver.get("https://demoqa.com/radio-button")
    time.sleep(2)
    driver.find_element(*YES_BUTTON).click()
    text = driver.find_element(*TEXT_YES).text
    time.sleep(2)
    assert text == "Yes"
    driver.find_element(*IMPRESSIVE_BUTTON).click()
    text = driver.find_element(*TEXT_YES).text
    time.sleep(2)
    assert text == "Impressive"
    driver.find_element(*NO_BUTTON).click()
    text = driver.find_element(*TEXT_YES).text
    time.sleep(2)

    assert text != "No"
