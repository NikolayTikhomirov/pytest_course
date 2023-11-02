import time

from data.urls import BaseUrl
from pages.interactions_page import InteractionPage


class TestInteractions:
    url = BaseUrl

    def test_drag_and_drop(self, driver):
        page = InteractionPage(driver, self.url.base_url)
        time.sleep(2)
        page.open_browser()
        page.drop_simple()

    def test_google(self, driver):
        page = InteractionPage(driver, self.url.google_url)
        page.open_browser()
        time.sleep(5)
