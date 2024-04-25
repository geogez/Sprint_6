from selenium import webdriver
import pytest
from data import Site


@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    driver.get(Site.scooter)
    yield driver
    driver.quit()
