import time

from locators.locators_alert import AlertPageLocators
from pages.base_page import BasePage


class Alert(BasePage):
    locators = AlertPageLocators()

    def simple_alert_button(self):
        self.element_is_visible(self.locators.SIMPLE_ALERT).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def alert_after_5_seconds(self):
        self.element_is_visible(self.locators.ALERT_AFTER_FIVE_SECOND).click()
        time.sleep(5)
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def confirm_cancel(self):
        self.element_is_visible(self.locators.CONFIRM_BOX).click()
        alert_window = self.driver.switch_to.alert
        alert_window.dismiss()
        text = self.element_is_visible(self.locators.CONFIRM_BOX_ANSWER)
        return text.text

    def confirm_ok(self):
        self.element_is_visible(self.locators.CONFIRM_BOX).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text = self.element_is_visible(self.locators.CONFIRM_BOX_ANSWER)
        return text.text

    def prompt(self):
        text = "Hello"
        self.element_is_visible(self.locators.PROMPT_BOX).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_message = self.element_is_visible(self.locators.PROMPT_BOX_ANSWER)
        return text, text_message.text
