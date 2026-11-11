import allure
import pytest
from playwright.sync_api import expect

from framework.data import BACKPACK, BIKE_LIGHT

pytestmark = allure.feature("Inventory")


@pytest.mark.smoke
@allure.title("Adding a product updates the cart badge and swaps the button to Remove")
def test_add_product_updates_cart_badge(inventory):
    inventory.add_to_cart(BACKPACK)

    expect(inventory.cart_badge).to_have_text("1")
    expect(inventory.remove_button(BACKPACK)).to_be_visible()


@pytest.mark.regression
@allure.title("Removing a product from the inventory page clears the cart badge")
def test_remove_product_clears_badge(inventory):
    inventory.add_to_cart(BACKPACK)
    inventory.remove_button(BACKPACK).click()

    expect(inventory.cart_badge).to_have_count(0)
    expect(inventory.add_to_cart_button(BACKPACK)).to_be_visible()


@pytest.mark.regression
@pytest.mark.parametrize("option, reverse", [("price_asc", False), ("price_desc", True)])
@allure.title("Products can be sorted by price ({option})")
def test_sort_by_price(inventory, option, reverse):
    inventory.sort_by(option)

    prices = inventory.prices()
    assert prices == sorted(prices, reverse=reverse)


@pytest.mark.regression
@pytest.mark.parametrize("option, reverse", [("name_asc", False), ("name_desc", True)])
@allure.title("Products can be sorted by name ({option})")
def test_sort_by_name(inventory, option, reverse):
    inventory.sort_by(option)

    names = inventory.names()
    assert names == sorted(names, reverse=reverse)


@pytest.mark.regression
@allure.title("Cart badge counts multiple products")
def test_cart_badge_counts_multiple_items(inventory):
    inventory.add_to_cart(BACKPACK, BIKE_LIGHT)

    expect(inventory.cart_badge).to_have_text("2")
