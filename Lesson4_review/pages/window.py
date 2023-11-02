import time

from locators.locators_window import WindowPageLocators
from pages.base_page import BasePage


class WindowPage(BasePage):
    locators = WindowPageLocators()

    def check_opened_new_tab(self):
        self.element_is_clickable(self.locators.NEW_TAB).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text = self.element_is_visible(self.locators.NEW_TAB_PAGE).text
        return text

    def check_opened_new_window(self):
        self.element_is_clickable(self.locators.NEW_WINDOW).click()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        text = self.element_is_visible(self.locators.NEW_TAB_PAGE).text
        return text
