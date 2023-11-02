import time

from locators.locators_interactions import InteractionsLocators
from pages.base_page import BasePage


class InteractionPage(BasePage):
    locators = InteractionsLocators

    def drop_simple(self):
        time.sleep(2)
        drag_div = self.element_is_visible(self.locators.DRAG)
        drop_div = self.element_is_visible(self.locators.DROP)
        self.drag_and_drop(drag_div, drop_div)
        text = self.element_is_visible(self.locators.DROP_TEXT).text
        assert text == "Dropped!"
