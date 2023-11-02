from selenium.webdriver.common.by import By


class FramePageLocators:
    FRAME_PAGE = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
    FRAME = {
        "big": (By.CSS_SELECTOR, "iframe[id='frame1']"),
        "small": (By.CSS_SELECTOR, "iframe[id='frame2']")
    }