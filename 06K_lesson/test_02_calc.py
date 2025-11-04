from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

input_field = driver.find_element(By.ID, 'delay')
input_field.clear()
input_field.send_keys("45")

driver.find_element(By.XPATH, "//span[text()='7']").click()
driver.find_element(By.XPATH, "//span[text()='+']").click()
driver.find_element(By.XPATH, "//span[text()='8']").click()
driver.find_element(By.XPATH, "//span[text()='=']").click()

WebDriverWait(driver, 45).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
)

driver.quit()