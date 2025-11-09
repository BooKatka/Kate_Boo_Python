from selenium import webdriver
from Class.Calculator_page import CalculatorPage


def test_form_calculator():
    driver = webdriver.Chrome()
    calculator_page = CalculatorPage(driver)

    calculator_page.delay()
    to_be = calculator_page.sum_of_the_numbers()
    wait_result = calculator_page.get_result()
    calculator_page.close_driver()

    assert wait_result == to_be
