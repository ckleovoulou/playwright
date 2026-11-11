import allure
from playwright.sync_api import Locator, Page


class BasePage:
    """Shared behaviour for all page objects.

    Rules (see AGENTS.md): page objects expose locators and actions only.
    Assertions live in tests, using Playwright's auto-waiting `expect`.
    """

    path = "/"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        with allure.step(f"Open {self.__class__.__name__} ({self.path})"):
            self.page.goto(self.path)
        return self

    @property
    def title(self) -> Locator:
        return self.page.locator(".title")

    @property
    def cart_badge(self) -> Locator:
        return self.page.locator(".shopping_cart_badge")
