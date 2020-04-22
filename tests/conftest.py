import pytest
from selenium import webdriver
driver = None
# https://docs.pytest.org/en/2.7.3/example/simple.html?highlight=addoption
# driver = None


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
        help="my option: chrome or firefox")


# zde nastavujeme to co se má dít před spuštěním každého testu
# tato fixtura(def setup) bude připojena na naši end2end testovací třídu


@pytest.fixture(scope="class")
def setup(request):
    global driver # je globální kdyby byl potřeba pro jiné metody v této třídě

    browser = request.config.getoption("browser")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    # následujícím řádkem transformujeme local driver na class driver
    # kdykoliv nekdo pouzije tuto fixturu, v tu chvíli se tento driver přiřadí do příslušné třídy(metody ap.)
    # to znamena, ze uz nemusime nic vracet v teto metode
    request.cls.driver = driver
    # yeild zaridi, aby se kod pred nim provedl na zacatku testu a kod po nem po dokonceni testu
    yield
    driver.close()

