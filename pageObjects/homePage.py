from selenium.webdriver.common.by import By
# TODO check OOP self vs ClassName
from pageObjects.checkoutPage import CheckoutPage

class HomePage:
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    ice_creams_check = (By.ID, "exampleCheck1")
    gender_select = (By.ID, "exampleFormControlSelect1")
    submit_button = (By.XPATH, "//input[@value='Submit']")
    success = (By.CSS_SELECTOR, "[class*='alert-success']")

    def __init__(self, driver):
        self.driver = driver

    def shop_items(self):
        # self.driver.find_element_by_css_selector("a[href*='shop']").click()
        self.driver.find_element(*HomePage.shop).click() # hvezdicka je tuple deserialization
        return CheckoutPage(self.driver)

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_ice_cream_check(self):
        return self.driver.find_element(*HomePage.ice_creams_check)

    def get_gender_select(self):
        return self.driver.find_element(*HomePage.gender_select)

    def get_submit_button(self):
        return self.driver.find_element(*HomePage.submit_button)

    def get_alert_success_paragraph(self):
        return self.driver.find_element(*HomePage.success)