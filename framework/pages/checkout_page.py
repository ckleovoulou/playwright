import allure

from framework.data import Customer
from framework.pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Covers the three checkout steps: your information, overview, complete."""

    path = "/checkout-step-one.html"

    # Step one: your information
    @property
    def first_name(self):
        return self.page.get_by_placeholder("First Name")

    @property
    def last_name(self):
        return self.page.get_by_placeholder("Last Name")

    @property
    def postal_code(self):
        return self.page.get_by_placeholder("Zip/Postal Code")

    @property
    def continue_button(self):
        return self.page.get_by_role("button", name="Continue")

    @property
    def error(self):
        return self.page.get_by_test_id("error")

    # Step two: overview
    @property
    def item_total(self):
        return self.page.locator(".summary_subtotal_label")

    @property
    def finish_button(self):
        return self.page.get_by_role("button", name="Finish")

    # Complete
    @property
    def complete_header(self):
        return self.page.locator(".complete-header")

    def fill_information(self, customer: Customer) -> "CheckoutPage":
        with allure.step("Fill customer information"):
            self.first_name.fill(customer.first_name)
            self.last_name.fill(customer.last_name)
            self.postal_code.fill(customer.postal_code)
            self.continue_button.click()
        return self

    def finish(self) -> "CheckoutPage":
        with allure.step("Finish order"):
            self.finish_button.click()
        return self
