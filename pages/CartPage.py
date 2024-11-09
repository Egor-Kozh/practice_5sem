class CartPage:
    def __init__(self, page):
        self.page = page
        self.inventoty_item = page.locator("[data-test=\"inventory-item\"]")
        self.order = page.locator("[data-test=\"checkout\"]")

    def create_order(self):
        self.order.click()