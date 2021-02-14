link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_presence_add_to_basket_button(browser):
    browser.get(link)
    assert browser.find_elements_by_class_name("btn-add-to-basket"), "There is no 'Add to basket' button on the page"
