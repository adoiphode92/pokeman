import pytest
from selenium import webdriver
from page_objects.login_page import LoginPage  # Import POM class

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Change to your browser (Chrome, Firefox, Edge)
    driver.get("https://example.com/login")  # Replace with actual login URL
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("valid_user", "valid_password")
    assert "dashboard" in driver.current_url  # Verify successful login

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("invalid_user", "wrong_password")
    assert "error" in driver.page_source  # Verify error message appears

def test_empty_fields(driver):
    login_page = LoginPage(driver)
    login_page.login("", "")
    assert "This field is required" in driver.page_source  # Adjust assertion based on error message

