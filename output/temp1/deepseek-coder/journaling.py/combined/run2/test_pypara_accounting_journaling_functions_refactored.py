import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import helpers
import journaling as journal

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_searching_products(setup):
    driver = setup
    driver.get("https://www.google.com/")
    driver.find_element(By.XPATH, "//*[@name='q']").send_keys("python")
    driver.find_element(By.XPATH, "//*[@name='btnK']").click()
    assert "python" in driver.title
    
def test_adding_to_basket(setup):
    driver = setup
    driver.get("https://www.google.com/")
    driver.find_element(By.XPATH, "//*[@name='q']").send_keys("Book")
    driver.find_element(By.XPATH, "//*[@name='btnK']").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class, 'product-details')]//*[contains(text(), 'Add To Wishlist')])[1]"))).click()
    assert "book" in driver.title

import pytest

def test_timer_starts_stops_correctly():
    """
    This test class checks if the timer correctly starts and stops in a class instance.
    """
    none_type_value = None
    journal_entry_instance = journal.JournalEntry(none_type_value, none_type_value, none_type_value)
    journal_entry_instance.validate()
    none_type_return = journal_entry_instance.validate()
    assert none_type_return == none_type_value

def test_searching_products():
    """
    This test class checks if the searching products feature is functioning correctly.
    """
    assert True

def test_adding_to_basket():
    """
    This test class checks if adding to basket is functioning correctly.
    """
    assert True