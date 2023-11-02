import pytest

from pages.frame_page import FramePage


class TestFrame:

    @pytest.mark.parametrize("size", ["big", "small"])
    def test_big_frame(self, driver, size):
        page = FramePage(driver, "https://demoqa.com/frames")
        page.open_browser()
        data = page.get_frame_size(size=size)
        width, height, text = page.frame(size=size)
        assert width == data["width"] and height == data["height"]
        assert text == "This is a sample page"
