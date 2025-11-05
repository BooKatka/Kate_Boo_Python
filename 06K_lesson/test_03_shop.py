import pytest
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_shop():
    driver = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()))
    
    driver.get("https://www.saucedemo.com/")
    WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "user-name"))
    )

    login_data = {
    'user-name': "standard_user",
    'password': "secret_sauce"
    }

    for field_id, value in login_data.items():
        input_field = driver.find_element(By.ID, field_id)
        input_field.send_keys(value)

    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.CSS_SELECTOR, "input#login-button").click()

    driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
    driver.find_element(By.CSS_SELECTOR, "button#checkout").click()

    form_data = {
    'first-name': "Екатерина",
    'last-name': "Бурученко",
    'zip-code': "660118"
    }

    for field_id, value in form_data.items():
    input_field = driver.find_element(By.ID, field_id)
    input_field.send_keys(value)

    driver.find_element(By.ID, "continue").click()

    ttl = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
    assert "Total: $58.29" in ttl

    driver.quit()
