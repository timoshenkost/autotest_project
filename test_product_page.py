from .pages.product_page import ProductPage
from time import sleep
import pytest
from selenium.common.exceptions import NoAlertPresentException


links = [
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
         ]

@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.compare_name_and_name_added_to_basket()
    page.compare_price_and_price_to_basket()