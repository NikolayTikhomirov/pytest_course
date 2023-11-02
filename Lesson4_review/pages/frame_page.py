from locators.locators_frame import FramePageLocators
from pages.base_page import BasePage


class FramePage(BasePage):
    locators = FramePageLocators()

    def frame(self, size):
        locator = self.locators.FRAME[size]
        frame = self.element_is_presence(locator)
        width = frame.get_attribute("width")
        height = frame.get_attribute("height")
        self.driver.switch_to.frame(frame)
        text = self.element_is_presence(self.locators.FRAME_PAGE).text
        return width, height, text

    def get_frame_size(self, size):
        data = {
            "big": {
                "width": "500px",
                "height": "350px"
            },
            "small": {
                "width": "100px",
                "height": "100px"
            }
        }
        return data[size]
