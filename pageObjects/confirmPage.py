from selenium.webdriver.common.by import By


class ConfirmPage:
    delivery_location = (By.ID, "country")
    country = (By.LINK_TEXT, "India")
    terms_conditions = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase = (By.CSS_SELECTOR, "[type='submit']")
    success = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver):
        self.driver = driver

    def get_delivery_location(self):
        return self.driver.find_element(*ConfirmPage.delivery_location)

    def get_country(self):
        return self.driver.find_element(*ConfirmPage.country)

    def get_terms_and_conditions(self):
        return self.driver.find_element(*ConfirmPage.terms_conditions)

    def get_purchase_button(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def get_success_paragraph(self):
        return self.driver.find_element(*ConfirmPage.success)
