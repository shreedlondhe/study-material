import pytest
from selenium import webdriver

driver = None


@pytest.fixture
def setup():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield
    print(driver.title)
    driver.close()


def test_1(setup):
    driver.get("https://facebook.com")
    print("Perform test")


def test_2(setup):
    driver.get("https://gmail.com")
    print("Perform test")


def test_3(setup):
    driver.get("https://amazon.com")
    print("Perform test")
