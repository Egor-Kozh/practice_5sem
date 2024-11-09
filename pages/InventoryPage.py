class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.add_backpack = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.cart = page.locator("[data-test=\"shopping-cart-link\"]")
        self.delete_backpack = page.locator("[data-test=\"remove-sauce-labs-backpack\"]")

    def add_to_cart(self):
        self.add_backpack.click()

    def check_cart(self):
        self.cart.click()

    def delete_cart(self):
        self.delete_backpack.click()