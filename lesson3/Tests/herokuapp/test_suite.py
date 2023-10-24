import locators as L
import global_variables as GV

def test_add_2_remove_1_element(driver):
    # All delete buttons the same and located in 1 div element
    def number_of_del_buttons():
        container = driver.find_element(*L.DELETE_BUTTONS_CONTAINER)
        num_of_del_buttons = len(container.find_elements(*L.ANY_CHILD_ELEMENT))
        return num_of_del_buttons

    driver.get(GV.ADD_REMOVE_ELEMENTS_PAGE)
    assert driver.current_url == GV.ADD_REMOVE_ELEMENTS_PAGE

    assert number_of_del_buttons() == 0

    driver.find_element(*L.ADD_ELEMENT_BUTTON).click()
    assert number_of_del_buttons() == 1

    driver.find_element(*L.ADD_ELEMENT_BUTTON).click()
    assert number_of_del_buttons() == 2

    driver.find_element(*L.DELETE_ELEMENT_BUTTON).click()
    assert number_of_del_buttons() == 1

def test_basic_auth(driver):
    driver.get(f"http://{GV.LOGIN}:{GV.PASSWORD}@{GV.BASIC_AUTH_PAGE[8:]}")
    assert driver.find_element(*L.AUTH_MESSAGE).text == GV.AUTH_MESSAGE_TEXT

def test_broken_images(driver):
    driver.get(GV.BROKEN_IMAGES_PAGE)
    assert driver.current_url == GV.BROKEN_IMAGES_PAGE

    container = driver.find_element(*L.IMAGE_CONTAINER)
    all_img_sources = container.find_elements(*L.IMG_CHILD_ELEMENTS)
    broken_img_count = 0
    correct_img_count = 0

    for i in all_img_sources:
        url = i.get_attribute("src")
        if url.startswith(GV.IMG_ROOT_PATH):
            correct_img_count += 1
        else:
            broken_img_count += 1
    print(f"\nFrom {len(all_img_sources)} images, {broken_img_count} broken and {correct_img_count} correct")
    assert correct_img_count == 1

def test_checkbox(driver):
    driver.get(GV.CHECKBOXES_PAGE)
    assert driver.current_url == GV.CHECKBOXES_PAGE
    assert driver.find_element(*L.CHECKBOX_1).get_attribute("checked") is None
    assert driver.find_element(*L.CHECKBOX_2).get_attribute("checked")

    driver.find_element(*L.CHECKBOX_1).click()
    assert driver.find_element(*L.CHECKBOX_1).get_attribute("checked")

    driver.find_element(*L.CHECKBOX_2).click()
    assert driver.find_element(*L.CHECKBOX_2).get_attribute("checked") is None
