"""Test data shared across tests. Keep data here, not hard-coded inside tests."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    name: str
    slug: str  # used by Sauce Demo in data-test ids, e.g. add-to-cart-<slug>
    price: float


BACKPACK = Product("Sauce Labs Backpack", "sauce-labs-backpack", 29.99)
BIKE_LIGHT = Product("Sauce Labs Bike Light", "sauce-labs-bike-light", 9.99)
BOLT_TSHIRT = Product("Sauce Labs Bolt T-Shirt", "sauce-labs-bolt-t-shirt", 15.99)


@dataclass(frozen=True)
class Customer:
    first_name: str
    last_name: str
    postal_code: str


CUSTOMER = Customer("Chris", "Tester", "3036")

ERRORS = {
    "locked_out": "Epic sadface: Sorry, this user has been locked out.",
    "bad_credentials": "Epic sadface: Username and password do not match any user in this service",
    "username_required": "Epic sadface: Username is required",
    "password_required": "Epic sadface: Password is required",
    "postal_code_required": "Error: Postal Code is required",
}
