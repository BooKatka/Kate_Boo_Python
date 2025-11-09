from selenium.webdriver.common.by import By


class ShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/')
        self.driver.implicitly_wait(5)

    # Авторизация
    def autorization(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    # Добавление товара в корзину
    def add(self):
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    # Работа в корзине, оформление покупки
    def shopping_cart_and_checkout(self):
        self.driver.find_element(By.ID, "shopping_cart_container").click()
        self.driver.find_element(By.ID, "checkout").click()

    # Заполнение формы на оплату
    def form_of_payment(self):
        self.driver.find_element(By.ID, "first-name").send_keys('Екатерина')
        self.driver.find_element(By.ID, "last-name").send_keys('Бурученко')
        self.driver.find_element(By.ID, "postal-code").send_keys('660118')
        self.driver.find_element(By.ID, "continue").click()

    # Итоговая цена покупок
    def total_price(self):
        self.driver.find_element(
            By.CSS_SELECTOR, ".summary_total_label").text