import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(executable_path='PycharmProjects\TEST2\chromedriver.exe')
    driver.maximize_window()
    yield driver
    driver.quit()