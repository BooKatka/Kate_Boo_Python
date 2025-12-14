import pytest
from selenium import webdriver
from Shop_page_l10 import Shop_l10
import allure  # Подключение библиотеки Allure


@allure.epic("Интернет- магазин — авто-тест покупки в онлайн магазина")
@pytest.fixture(scope='module')
@allure.title("Инициализация ВД Chrome")
def chrome_driver():
    """
    Фикстура инициализации драйвера браузера Chrome
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.feature("Процесс оформления заказа")  # Общая характеристика
@allure.story("Автоматическая покупка товара")  # История внутри
@allure.description("""
Тест полного цикла покупки:
1. Авторизация
2. Выбор товаров
3. Оформление заказа
""")  # Детальное описание цели теста
@allure.severity(allure.severity_level.NORMAL)  # Уровень важности теста
def test_checkout_process(chrome_driver):
    """
    Авторизация, покупка товаров и проверка итоговой стоимости
    """
    page = Shop_l10(chrome_driver)
# Первый шаг
    with allure.step("Переход на главную страницу"):
        page.go_home()
# 2 шаг
    with allure.step("Авторизация стандартным пользователем"):
        page.login('standard_user', 'secret_sauce')
# 3 шаг
    with allure.step("Ожидание загрузки списка товаров"):
        page.wait_until_products_loaded()
# 4 шаг
    with allure.step("Добавление товаров в корзину"):
        products = {
            'Sauce Labs Backpack': 'add-to-cart-sauce-labs-backpack',
            'Sauce Labs Bolt T-Shirt': 'add-to-cart-sauce-labs-bolt-t-shirt',
            'Sauce Labs Onesie': 'add-to-cart-sauce-labs-onesie'
        }
        page.add_items_to_cart(products)
# 5 шаг
    with allure.step("Переход в корзину"):
        page.go_to_cart()
# 6 шаг
    with allure.step("Начало оформления заказа"):
        page.start_checkout()
# 7 шаг
    with allure.step("Заполнение данных покупателя"):
        page.fill_billing_details('John', 'Doe', '12345')
# 8 шаг
    with allure.step("Проверяка итоговой суммы ($58.29)"):
        page.check_total_amount('$58.29')
# 9 шаг
    with allure.step("Завершение покупки"):
        page.complete_order()
