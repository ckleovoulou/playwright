import allure

from framework.data import Product
from framework.pages.base_page import BasePage


class CartPage(BasePage):
    path = "/cart.html"

    @property
    def items(self):
        return self.page.locator(".cart_item")

    @property
    def item_names(self):
        return self.page.locator(".cart_item .inventory_item_name")

    @property
    def checkout_button(self):
        return self.page.get_by_role("button", name="Checkout")

    def remove(self, product: Product) -> "CartPage":
        with allure.step(f"Remove '{product.name}' from cart"):
            self.page.get_by_test_id(f"remove-{product.slug}").click()
        return self

    def checkout(self):
        from framework.pages.checkout_page import CheckoutPage

        with allure.step("Start checkout"):
            self.checkout_button.click()
        return CheckoutPage(self.page)
