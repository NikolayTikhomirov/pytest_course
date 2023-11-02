import base64
import os
import time
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


def element_is_clickable(driver, locator, timeout=10):
    return wait(driver, timeout).until(EC.element_to_be_clickable(locator))


def element_is_visible(driver, locator, timeout=10):
    return wait(driver, timeout).until(EC.visibility_of_element_located(locator))


def element_is_presence(driver, locator, timeout=10):
    return wait(driver, timeout).until(EC.presence_of_element_located(locator))


def open_browser(driver, url):
    driver.get(url)


def test_upload(driver):
    open_browser(driver, "https://demoqa.com/upload-download")
    time.sleep(2)
    get_path()
    file_name, current_dir = get_path()
    locator = (By.CSS_SELECTOR, "input[id='uploadFile']")
    element_is_visible(driver=driver, locator=locator).send_keys(current_dir)
    UPLOADED_FILE = (By.CSS_SELECTOR, "p[id='uploadedFilePath']")
    text = element_is_visible(driver=driver, locator=UPLOADED_FILE)
    time.sleep(2)
    print(f"text : {text.text}")
    print(f"current_dir: {current_dir}")
    os.remove(current_dir)
    assert file_name in text.text


def get_path():
    path = os.path.dirname(os.path.abspath(__file__))
    file_name = "test.txt"
    current_dir = os.path.join(path, file_name)
    print(current_dir)
    with open(current_dir, 'w+') as file:
        file.write("Hello")
    return file_name, current_dir


def test_download_file(driver):
    open_browser(driver, "https://demoqa.com/upload-download")
    DOWNLOAD_FILE = (By.CSS_SELECTOR, "a[id='downloadButton']")
    path = os.path.dirname(os.path.abspath(__file__))
    file_name = f"test{random.randint(1, 100)}.png"
    current_dir = os.path.join(path, file_name)
    link = element_is_visible(driver=driver, locator=DOWNLOAD_FILE).get_attribute('href')
    link_b = base64.b64decode(link)
    with open(current_dir, 'wb+') as f:
        offset = link_b.find(b'\xff\xd8')
        f.write(link_b[offset:])
        check_file = os.path.exists(current_dir)
    os.remove(current_dir)
