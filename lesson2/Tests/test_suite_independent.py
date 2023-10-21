from global_variables import INVENTORY_PAGE
def test_successful_login(site_auth, driver):
    assert driver.current_url == INVENTORY_PAGE
