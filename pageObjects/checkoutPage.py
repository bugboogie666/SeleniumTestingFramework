from selenium.webdriver.common.by import By
from pageObjects.confirmPage import ConfirmPage

class CheckoutPage:
    products = (By.XPATH, "//div[@class='card h-100']")
    buttons = (By.XPATH, "//button[text()='Add ']")
    checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    final_checkout_button = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def get_products(self):
        return self.driver.find_elements(*CheckoutPage.products)

    def get_add_buttons(self):
        return self.driver.find_elements(*CheckoutPage.buttons)

    def get_checkout(self):
        return self.driver.find_element(*CheckoutPage.checkout_button)

    def get_final_checkout(self):
        self.driver.find_element(*CheckoutPage.final_checkout_button).click()
        return ConfirmPage(self.driver)


