import pytest
from utilities.BaseClass import BaseClass
import testData.DataFactory
from selenium.webdriver.common.by import By
from pageObjects.homePage import HomePage
from testData.DataFactory import DataFactory

# TODO: implementovat proměnné místo 'hardcoded' hodnot - done
# TODO: brát si hodnoty z externího zdroje třídy DataFactory - done
# TODO: oddebugovat, proč se loguje druhý data set('Tereza') do logu 2x

class TestHomePage(BaseClass):

    def test_form_submission(self, get_test_data): # get test data si takto v podobě parametru funkce zavoláme z fixtury

        log = self.get_logger()
        home_page = HomePage(self.driver)
        self.driver.maximize_window()
        log.info(f"first name: {get_test_data['firstname']}")
        home_page.get_name().send_keys(get_test_data['firstname'])
        log.info(f"first name: {get_test_data['email']}")
        home_page.get_email().send_keys(get_test_data['email'])
        home_page.get_ice_cream_check().click()
        self.select_combobox_value(home_page.get_gender_select(), get_test_data['gender'])
        home_page.get_submit_button().click()
        # self.verify_link_presence(By.CSS_SELECTOR, "[class*='alert-success']")
        alert_text = home_page.get_alert_success_paragraph().text

        assert ("Success" in alert_text)

        self.driver.refresh()

    # jako data je možno do fixtury vložit i tuple, ale pak bychom je volali v testu přes index, což se špatně čte
    @pytest.fixture(params=DataFactory.get_homepage_data())
    def get_test_data(self, request):
        return request.param


