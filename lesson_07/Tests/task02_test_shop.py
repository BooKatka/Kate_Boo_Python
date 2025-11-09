from selenium import webdriver
from Class.Shop import ShopPage


def test_ShopPage():
    driver = webdriver.Chrome()
    pur_page = ShopPage(driver)

    price = pur_page.autorization()
    pur_page.add()
    pur_page.shopping_cart_and_checkout()
    pur_page.form_of_payment()
    total_price = pur_page.total_price()

    assert price == total_price