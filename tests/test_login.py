from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_valid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login()

    products = ProductsPage(driver)
    assert products.is_open()

def test_invalid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login("wrong_user", "wrong_password")

    assert "Username and password do not match" in login.get_error()
