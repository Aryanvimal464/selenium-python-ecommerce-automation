from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_add_product_to_cart(driver):
    login = LoginPage(driver)
    login.open()
    login.login()

    products = ProductsPage(driver)
    assert products.is_open()
    products.add_backpack_to_cart()
    assert products.cart_count() == "1"

    products.open_cart()
    cart = CartPage(driver)
    assert "Sauce Labs Backpack" in cart.item_names()
