from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):
    TITLE = (By.CSS_SELECTOR, ".title")
    BACKPACK_ADD = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def is_open(self):
        return self.get_text(self.TITLE) == "Products"

    def add_backpack_to_cart(self):
        self.click(self.BACKPACK_ADD)

    def cart_count(self):
        return self.get_text(self.CART_BADGE)

    def open_cart(self):
        self.click(self.CART_LINK)
