import allure
import pytest
from playwright.sync_api import expect

from framework.data import BACKPACK, BIKE_LIGHT, BOLT_TSHIRT, CUSTOMER, ERRORS, Customer

pytestmark = allure.feature("Checkout")


@pytest.mark.smoke
@allure.title("User can buy a product end to end")
def test_complete_purchase(inventory):
    checkout = inventory.add_to_cart(BACKPACK).go_to_cart().checkout()
    checkout.fill_information(CUSTOMER)

    expect(checkout.item_total).to_have_text(f"Item total: ${BACKPACK.price}")

    checkout.finish()

    expect(checkout.complete_header).to_have_text("Thank you for your order!")
    expect(checkout.cart_badge).to_have_count(0)


@pytest.mark.regression
@allure.title("Cart shows exactly the products that were added")
def test_cart_lists_added_products(inventory):
    cart = inventory.add_to_cart(BACKPACK, BOLT_TSHIRT).go_to_cart()

    expect(cart.item_names).to_have_text([BACKPACK.name, BOLT_TSHIRT.name])


@pytest.mark.regression
@allure.title("Removing a product in the cart leaves the others")
def test_remove_item_in_cart(inventory):
    cart = inventory.add_to_cart(BACKPACK, BIKE_LIGHT).go_to_cart()
    cart.remove(BACKPACK)

    expect(cart.item_names).to_have_text([BIKE_LIGHT.name])
    expect(cart.cart_badge).to_have_text("1")


@pytest.mark.regression
@allure.title("Item total adds up the prices of all products")
def test_item_total_sums_prices(inventory):
    checkout = inventory.add_to_cart(BACKPACK, BIKE_LIGHT).go_to_cart().checkout()
    checkout.fill_information(CUSTOMER)

    expected = round(BACKPACK.price + BIKE_LIGHT.price, 2)
    expect(checkout.item_total).to_have_text(f"Item total: ${expected}")


@pytest.mark.regression
@allure.title("Checkout requires a postal code")
def test_checkout_requires_postal_code(inventory):
    checkout = inventory.add_to_cart(BACKPACK).go_to_cart().checkout()
    checkout.fill_information(Customer(CUSTOMER.first_name, CUSTOMER.last_name, ""))

    expect(checkout.error).to_have_text(ERRORS["postal_code_required"])
