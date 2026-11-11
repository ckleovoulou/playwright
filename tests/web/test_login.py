import re

import allure
import pytest
from playwright.sync_api import expect

from framework.config import LOCKED_OUT_USER, PASSWORD, STANDARD_USER
from framework.data import ERRORS

pytestmark = allure.feature("Login")


@pytest.mark.smoke
@allure.title("Standard user can log in and sees the product list")
def test_valid_login(login_page):
    inventory = login_page.login_as(STANDARD_USER)

    expect(login_page.page).to_have_url(re.compile(r"/inventory\.html$"))
    expect(inventory.title).to_have_text("Products")


@pytest.mark.regression
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        pytest.param(LOCKED_OUT_USER.username, PASSWORD, ERRORS["locked_out"], id="locked-out-user"),
        pytest.param(
            STANDARD_USER.username, "wrong_password", ERRORS["bad_credentials"], id="wrong-password"
        ),
        pytest.param("", PASSWORD, ERRORS["username_required"], id="empty-username"),
        pytest.param(STANDARD_USER.username, "", ERRORS["password_required"], id="empty-password"),
    ],
)
@allure.title("Login is rejected with a clear error: {expected_error}")
def test_invalid_login(login_page, username, password, expected_error):
    login_page.login(username, password)

    expect(login_page.error).to_have_text(expected_error)
    expect(login_page.login_button).to_be_visible()


@pytest.mark.regression
@allure.title("Protected pages redirect to login when not authenticated")
def test_inventory_requires_login(page):
    page.goto("/inventory.html")

    expect(page.get_by_test_id("error")).to_contain_text(
        "You can only access '/inventory.html' when you are logged in"
    )
