import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


def element_is_clickable(driver, locator, timeout=10):
    return wait(driver, timeout).until(EC.element_to_be_clickable(locator))


def element_is_visible(driver, locator, timeout=10):
    return wait(driver, timeout).until(EC.visibility_of_element_located(locator))


def element_is_presence(driver, locator, timeout=10):
    return wait(driver, timeout).until(EC.presence_of_element_located(locator))


def open(driver, url):
    driver.get(url)


def test_dynamic_button(driver):
    open(driver, "https://demoqa.com/dynamic-properties")
    button_loc = (By.CSS_SELECTOR, "button[id='enableAfter']")
    button = element_is_clickable(driver=driver, locator=button_loc)
    assert button.is_enabled()


def test_check_changed_color(driver):
    open(driver, "https://demoqa.com/dynamic-properties")
    time.sleep(2)
    locator = (By.CSS_SELECTOR, "button[id='colorChange']")
    button = element_is_presence(driver=driver, locator=locator)
    color_before = button.value_of_css_property("color")
    time.sleep(6)
    color_after = button.value_of_css_property("color")
    assert color_before != color_after


def test_button_is_visible_after_5_second(driver):
    open(driver, "https://demoqa.com/dynamic-properties")
    time.sleep(2)
    locator = (By.CSS_SELECTOR, "button[id='visibleAfter']")
    button = element_is_visible(driver=driver, locator=locator)
    assert button.is_displayed()


def test_get_attribute(driver):
    open(driver, "https://demoqa.com/links")
    time.sleep(2)
    locator = (By.CSS_SELECTOR, "a[id='simpleLink']")
    link = element_is_visible(driver=driver, locator=locator)
    attribute = link.get_attribute("target")
    print(attribute)


def test_new_tab(driver):
    open(driver, "https://demoqa.com/browser-windows")
    time.sleep(1)
    locator = (By.CSS_SELECTOR, "button[id='tabButton']")
    button = element_is_clickable(driver=driver, locator=locator)
    button.click()
    driver.switch_to.window(driver.window_handles[1])
    locator_text = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
    text = element_is_visible(driver=driver, locator=locator_text)
    time.sleep(4)
    print(text.text)

def test_alert(driver):
    open(driver, "https://demoqa.com/alerts")
    time.sleep(2)
    locator = (By.CSS_SELECTOR, "button[id='alertButton']")
    button = element_is_clickable(driver=driver, locator=locator)
    button.click()
    text = driver.switch_to.alert.text
    print(text)


def test_prompt(driver):
    open(driver, "https://demoqa.com/alerts")
    time.sleep(2)
    locator = (By.CSS_SELECTOR, "button[id='promtButton']")
    button = element_is_clickable(driver=driver, locator=locator)
    button.click()
    alert_window = driver.switch_to.alert
    alert_window.send_keys("test")
    time.sleep(2)
    alert_window.accept()
    locator_text = (By.CSS_SELECTOR, "span[id='promptResult']")
    text = element_is_visible(driver=driver, locator=locator_text).text
    time.sleep(4)
    assert "test" in text

def test_frame(driver):
    open(driver, "https://demoqa.com/frames")
    time.sleep(2)
    locator = (By.CSS_SELECTOR, "iframe[id='frame1']")
    iframe = element_is_visible(driver=driver, locator=locator)
    width = iframe.get_attribute("width")
    height = iframe.get_attribute("height")
    print(width)
    print(height)
    driver.switch_to.frame(iframe)
    locator_text = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
    text = element_is_visible(driver=driver, locator=locator_text)
    time.sleep(4)
    print(text.text)
