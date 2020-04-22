import re
import pytest
from tests import conftest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from pageObjects.homePage import HomePage

# py.test --html=report.html - tímto příkazem můžeme spustit test v CLI a vytvořit report v připravené HTML šabloně
# veskera magie je v conftestu a BaseClass


class TestOne(BaseClass):
    def test_e2e(self):

        log = self.get_logger()
        home_page = HomePage(self.driver)
        self.driver.maximize_window()
        # self.driver.find_element_by_css_selector("a[href*='shop']").click()
        checkout_page = home_page.shop_items()
        # products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        log.info("Getting all products")
        products = checkout_page.get_products()

        i = 0
        for product in products:
            # productName = product.find_element_by_xpath("div/h4/a").text
            product_name = re.search('^\D+[^\d]', product.text)[0] # TODO: odladit regex a odfiltrovat linebreaky nebo vhodněji definovat selector
            log.info(product_name)
            if "Blackberry" in product_name:
                # Add item into cart
                # product.find_elements_by_css_selector(".card-footer button")[i].click()
                checkout_page.get_add_buttons()[i].click()
            i += 1

        # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        checkout_page.get_checkout().click()
        # self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        confirm_page = checkout_page.get_final_checkout()
        # self.driver.find_element_by_id("country").send_keys("ind")
        log.info("Entering country name.")
        confirm_page.get_delivery_location().send_keys("ind")
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(ec.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verify_link_presence(By.LINK_TEXT, "India")
        # self.driver.find_element_by_link_text("India").click()
        confirm_page.get_country().click()
        # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        confirm_page.get_terms_and_conditions().click()
        # self.driver.find_element_by_css_selector("[type='submit']").click()
        confirm_page.get_purchase_button().click()
        # successText = self.driver.find_element_by_class_name("alert-success").text
        success_text = confirm_page.get_success_paragraph().text
        log.info(f"Text received from app is: {success_text}")

        assert "Success! Thank you!" in success_text

        self.driver.get_screenshot_as_file("screen.png")
