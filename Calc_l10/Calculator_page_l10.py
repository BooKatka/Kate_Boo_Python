import allure  # Импорт модуля allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("Калькулятор")
@allure.title("Инициализация ВД Chrome")
# Фикстура для запуска и остановки драйвера
@pytest.fixture(scope="module")
def chrome_driver():
    """
    Инициализации драйвера браузера Chrome
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.description("Проверка работы калькулятора с заданной задержкой")
@allure.feature("Тест калькулятора с задержкой")
@allure.severity(allure.severity_level.NORMAL)  # Уровень важности теста
@allure.story("Проверка функционала медленного калькулятора")
def test_calculator_with_delay(chrome_driver):
    """
    Автотест калькулятора с задержкой вычисления
    """
    with allure.step("Открытие страницы"):  # Открытие страницы
        chrome_driver.get(
            'https://bonigarcia.dev/'
            'selenium-webdriver-java/slow-calculator.html')

    with allure.step("Устанавка задержки на 45 секунд"):
        delay_input = chrome_driver.find_element(
            By.ID, 'delay')  # Задержка ввода
        delay_input.clear()
        delay_input.send_keys('45')

    with allure.step("Нажатие кнопок 7 + 8 ="):
        buttons_to_click = ['7', '+', '8', '=']
        for button_text in buttons_to_click:
            xpath_selector = f'//span[contains(text(), "{button_text}")]'
            button = chrome_driver.find_element(By.XPATH, xpath_selector)
            button.click()

    with allure.step("Ожидание результата 15"):
        WebDriverWait(chrome_driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"
                                             ))

    result_text = chrome_driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert "15" in result_text, f"Ожидаемый результат 15, получен:{
        result_text}"
