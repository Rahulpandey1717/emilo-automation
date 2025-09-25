import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # or use webdriver_manager
    driver.maximize_window()
    yield driver
    driver.quit()
