import allure
import pytest
from playwright.sync_api import Page

from framework.config import STANDARD_USER
from framework.pages import InventoryPage, LoginPage


@pytest.fixture(scope="session", autouse=True)
def _use_data_test_attribute(playwright):
    """Sauce Demo uses `data-test`, so make page.get_by_test_id() look for it."""
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture(autouse=True)
def _attach_screenshot_on_failure(request, page: Page):
    """Attach a full-page screenshot to the Allure report when a test fails."""
    yield
    report = getattr(request.node, "rep_call", None)
    if report and report.failed:
        allure.attach(
            page.screenshot(full_page=True),
            name="screenshot-on-failure",
            attachment_type=allure.attachment_type.PNG,
        )


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page).open()


@pytest.fixture
def inventory(login_page: LoginPage) -> InventoryPage:
    """Start the test already logged in as the standard user."""
    return login_page.login_as(STANDARD_USER)
