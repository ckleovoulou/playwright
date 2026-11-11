import allure

from framework.data import Product
from framework.pages.base_page import BasePage


class InventoryPage(BasePage):
    path = "/inventory.html"

    SORT_OPTIONS = {
        "name_asc": "az",
        "name_desc": "za",
        "price_asc": "lohi",
        "price_desc": "hilo",
    }

    @property
    def sort_dropdown(self):
        return self.page.locator("select.product_sort_container")

    @property
    def item_names(self):
        return self.page.locator(".inventory_item_name")

    @property
    def item_prices(self):
        return self.page.locator(".inventory_item_price")

    @property
    def cart_link(self):
        return self.page.locator(".shopping_cart_link")

    def add_to_cart_button(self, product: Product):
        return self.page.get_by_test_id(f"add-to-cart-{product.slug}")

    def remove_button(self, product: Product):
        return self.page.get_by_test_id(f"remove-{product.slug}")

    def add_to_cart(self, *products: Product) -> "InventoryPage":
        for product in products:
            with allure.step(f"Add '{product.name}' to cart"):
                self.add_to_cart_button(product).click()
        return self

    def sort_by(self, option: str) -> "InventoryPage":
        with allure.step(f"Sort products by {option}"):
            self.sort_dropdown.select_option(self.SORT_OPTIONS[option])
        return self

    def prices(self) -> list[float]:
        return [float(p.replace("$", "")) for p in self.item_prices.all_inner_texts()]

    def names(self) -> list[str]:
        return self.item_names.all_inner_texts()

    def go_to_cart(self):
        from framework.pages.cart_page import CartPage

        with allure.step("Open cart"):
            self.cart_link.click()
        return CartPage(self.page)
