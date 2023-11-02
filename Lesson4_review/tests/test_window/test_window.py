import time

from pages.window import WindowPage


class TestWindow:

    def test_new_tab(self, driver):
        page = WindowPage(driver, "https://demoqa.com/browser-windows")
        page.open_browser()
        text = page.check_opened_new_tab()
        assert text == "This is a sample page"

    def test_new_window(self, driver):
        page = WindowPage(driver, "https://demoqa.com/browser-windows")
        page.open_browser()
        text = page.check_opened_new_window()
        assert text == "This is a sample page"
