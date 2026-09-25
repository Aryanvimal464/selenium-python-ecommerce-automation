from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    TITLE = (By.CSS_SELECTOR, ".title")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")

    def item_names(self):
        return [e.text for e in self.driver.find_elements(*self.ITEM_NAMES)]

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)
