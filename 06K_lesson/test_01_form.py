from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = EdgeService(
    r'D:\SkyPro\Python Auto\repository_clone\edgedriver\msedgedriver.exe')
driver = webdriver.Edge(service=service)
driver.implicitly_wait(20)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "first-name"))
)

fields_and_locators = {
    'first-name': "Иван",
    'last-name': "Петров",
    'address': "Ленина, 55-3",
    'e-mail': "test@skypro.com",
    'phone': "+7985899998787",
    'zip-code': "",
    'city': "Москва",
    'country': "Россия",
    'job-position': "QA",
    'company': "SkyPro"
}

for key, value in fields_and_locators.items():
    input_field = driver.find_element(By.NAME, key)
    input_field.send_keys(value)

driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3").click()

zip = driver.find_element(By.ID, "zip-code")
assert "alert-danger" in zip.get_attribute("class")

for locator in fields_and_locators:
    if locator != 'zip-code':
        element = driver.find_element(By.ID, locator)
        assert "alert-success" in element.get_attribute("class")

driver.quit()