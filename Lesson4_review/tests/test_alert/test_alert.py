from pages.alert import Alert


class TestAlert:
    def test_simple_alert(self, driver):
        page = Alert(driver, "https://demoqa.com/alerts")
        page.open_browser()
        alert_text = page.simple_alert_button()
        print(alert_text)

    def test_alert_after_5_seconds(self, driver):
        page = Alert(driver, "https://demoqa.com/alerts")
        page.open_browser()
        alert_text = page.alert_after_5_seconds()
        print(alert_text)

    def test_confirm_cancel(self, driver):
        page = Alert(driver, "https://demoqa.com/alerts")
        page.open_browser()
        text = page.confirm_cancel()
        print(text)

    def test_confirm_ok(self, driver):
        page = Alert(driver, "https://demoqa.com/alerts")
        page.open_browser()
        text = page.confirm_ok()
        print(text)

    def test_prompt(self, driver):
        page = Alert(driver, "https://demoqa.com/alerts")
        page.open_browser()
        text, result = page.prompt()
        assert text in result
