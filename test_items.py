# pytest.exe -s --language=es test_items.py
# pytest.exe -s --language=fr test_items.py

import time
import sys

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_for_button_to_add_product_in_basket(browser):
    browser.get(link)
    if '--language=fr' in sys.argv: time.sleep(30)
    browser.implicitly_wait(10)
    basket_btn = browser.find_elements_by_class_name("btn-add-to-basket")    
    assert len(basket_btn) > 0, "Not found button to add product in basket!"  


