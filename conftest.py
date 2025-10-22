import pytest
from selenium import webdriver
from utils import login

# creamos un fixture para el driver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver