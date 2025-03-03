from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "username")  # Change locator as per your app
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login")

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).clear()
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).clear()
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        """Combination of all actions: Enter credentials and login."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
