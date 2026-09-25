from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_complete_checkout(driver):
    login = LoginPage(driver)
    login.open()
    login.login()

    products = ProductsPage(driver)
    products.add_backpack_to_cart()
    products.open_cart()

    cart = CartPage(driver)
    cart.checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_customer_details("Aryan", "Vimal", "226001")
    checkout.finish_order()

    assert checkout.confirmation() == "Thank you for your order!"
