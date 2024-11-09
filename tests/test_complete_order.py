from playwright.sync_api import Page, expect
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
from pages.OrderPage import OrderPage

def test_complete_oder(page: Page) -> None:
    login_page = LoginPage(page)
    shop = InventoryPage(page)
    cart = CartPage(page)
    order = OrderPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    shop.add_to_cart()
    shop.check_cart()
    cart.create_order()
    order.input("standard", "user", "123")
    order.order_finish()
    expect(order.complete).to_be_visible()
