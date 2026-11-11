import allure

from framework.config import User
from framework.pages.base_page import BasePage
from framework.pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    path = "/"

    @property
    def username(self):
        return self.page.get_by_placeholder("Username")

    @property
    def password(self):
        return self.page.get_by_placeholder("Password")

    @property
    def login_button(self):
        return self.page.get_by_role("button", name="Login")

    @property
    def error(self):
        return self.page.get_by_test_id("error")

    def login(self, username: str, password: str) -> None:
        with allure.step(f"Log in as '{username}'"):
            self.username.fill(username)
            self.password.fill(password)
            self.login_button.click()

    def login_as(self, user: User) -> InventoryPage:
        self.login(user.username, user.password)
        return InventoryPage(self.page)
