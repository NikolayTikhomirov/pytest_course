import time


def test_second(driver):
    driver.get("https://www.google.com/")
    time.sleep(5)


def test_second1(driver):
    driver.get("https://expired.badssl.com/")
    time.sleep(5)
