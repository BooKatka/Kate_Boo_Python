import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Интернет-магазин — полный цикл онлайн покупки")
# Фикстура для запуска и остановки драйвера
@pytest.fixture(scope="module")
@allure.title("Инициализация ВД Chrome")
def chrome_driver():
    '''
    Тест онлайн покупки в магазине.
    '''
    with allure.step("Запуск браузера"):
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        yield driver
    with allure.step("Закрытие браузера"):
        driver.quit()
@allure.description("Тест покупки в магазине")
@allure.feature("Процесс оформления заказа")
@allure.severity(allure.severity_level.NORMAL)
class Shop_l10:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Переход на главную страницу сайта")
    @allure.title("Вход на сайт")
    def go_home(self):
        """Переход на домашнюю страницу"""
        self.driver.get('https://www.saucedemo.com/')

    @allure.step("Авторизация на сайте")
    @allure.title("Авторизация на сайте")
    def login(self, username, password):
        """Авторизация на сайте"""
        username_field = self.driver.find_element(By.ID, 'user-name')
        password_field = self.driver.find_element(By.ID, 'password')
        login_button = self.driver.find_element(By.ID, 'login-button')

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

    @allure.step("Ожидание загрузки товаров на странице")
    @allure.title("Ожидание загрузки страницы")
    def wait_until_products_loaded(self):
        """Ожидание, пока товары прогрузятся на странице"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'inventory_item')))

    @allure.step("Добавление товаров в корзину")
    @allure.title("Добавление товаров в корзину")
    def add_items_to_cart(self, items):
        """Добавление выбранных товаров в корзину"""
        for item_id in items.values():
            add_cart_button = self.driver.find_element(By.ID, item_id)
            add_cart_button.click()

    @allure.step("Переход в корзину")
    @allure.title("Переход в корзину")
    def go_to_cart(self):
        """Переход в корзину"""
        cart_icon = self.driver.find_element(
            By.CLASS_NAME, 'shopping_cart_link')
        cart_icon.click()

    @allure.step("Начало оформления заказа")
    def start_checkout(self):
        """Начало оформление нашего заказа"""
        checkout_button = self.driver.find_element(By.ID, 'checkout')
        checkout_button.click()

    @allure.step("Заполнение формы доставки")
    @allure.title("Заполнение формы доставки")
    def fill_billing_details(self, first_name, last_name, zip_code):
        """Заполнение формы для доставки"""
        first_name_field = self.driver.find_element(By.ID, 'first-name')
        last_name_field = self.driver.find_element(By.ID, 'last-name')
        postal_code_field = self.driver.find_element(By.ID, 'postal-code')
        continue_button = self.driver.find_element(By.ID, 'continue')

        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        postal_code_field.send_keys(zip_code)
        continue_button.click()

    @allure.step("Проверка итоговой суммы заказа")
    @allure.title("Проверка итоговой суммы заказа")
    def check_total_amount(self, expected_total):
        """Проверка итоговой сумму заказа"""
        total_amount_element = self.driver.find_element(
            By.CLASS_NAME, 'summary_total_label')
        total_amount = total_amount_element.text.split(':')[1].strip()
        assert total_amount == expected_total
        f"Итого должно быть {expected_total}, но сумма равна '{total_amount}'"

    @allure.step("Завершение покупки")
    @allure.title("Завершение покупки")
    def complete_order(self):
        """Завершение покупки"""
        finish_button = self.driver.find_element(By.ID, 'finish')
        finish_button.click()
