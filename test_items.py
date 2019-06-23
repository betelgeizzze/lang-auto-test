import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_show_user_language_interface(browser):
    browser.get(link)
    time.sleep(30)
    assert  browser.find_element_by_css_selector("button.btn-add-to-basket")