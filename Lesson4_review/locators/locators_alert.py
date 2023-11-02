from selenium.webdriver.common.by import By


class AlertPageLocators:
    SIMPLE_ALERT = (By.CSS_SELECTOR, "button[id='alertButton']")
    ALERT_AFTER_FIVE_SECOND = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_BOX = (By.CSS_SELECTOR, "button[id='confirmButton']")
    CONFIRM_BOX_ANSWER = (By.CSS_SELECTOR, "span[id='confirmResult']")
    PROMPT_BOX = (By.CSS_SELECTOR, "button[id='promtButton']")
    PROMPT_BOX_ANSWER = (By.CSS_SELECTOR, "span[id='promptResult']")