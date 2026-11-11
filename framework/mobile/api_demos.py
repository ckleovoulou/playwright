"""Screen objects for Appium's ApiDemos Android app (io.appium.android.apis)."""

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

APP_PACKAGE = "io.appium.android.apis"


class BaseScreen:
    def __init__(self, driver, timeout: int = 15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def by_accessibility_id(self, value: str):
        return self.wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, value)))

    def scroll_to_text(self, text: str):
        """Scroll the current list until an element with this exact text is on screen."""
        selector = (
            "new UiScrollable(new UiSelector().scrollable(true))"
            f'.scrollIntoView(new UiSelector().text("{text}"))'
        )
        return self.wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, selector)))

    def open_item(self, label: str):
        with allure.step(f"Open '{label}'"):
            self.by_accessibility_id(label).click()
        return self


class HomeScreen(BaseScreen):
    CATEGORIES = ["Accessibility", "Animation", "App", "Content", "Graphics", "Media", "OS", "Text", "Views"]

    def category(self, name: str):
        return self.by_accessibility_id(name)

    def open_views(self) -> "ViewsScreen":
        self.open_item("Views")
        return ViewsScreen(self.driver)


class ViewsScreen(BaseScreen):
    def open_controls_light_theme(self) -> "ControlsScreen":
        with allure.step("Open Views > Controls > 1. Light Theme"):
            self.scroll_to_text("Controls").click()
            self.by_accessibility_id("1. Light Theme").click()
        return ControlsScreen(self.driver)


class ControlsScreen(BaseScreen):
    @property
    def text_field(self):
        return self.wait.until(EC.presence_of_element_located((AppiumBy.ID, f"{APP_PACKAGE}:id/edit")))

    def type_text(self, text: str) -> "ControlsScreen":
        with allure.step(f"Type '{text}' into the text field"):
            self.text_field.send_keys(text)
        return self
