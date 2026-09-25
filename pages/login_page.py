from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config import BASE_URL, USERNAME, PASSWORD

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        self.driver.get(BASE_URL)

    def login(self, username=USERNAME, password=PASSWORD):
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error(self):
        return self.get_text(self.ERROR_MESSAGE)
