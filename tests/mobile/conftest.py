import os
import urllib.request
from pathlib import Path

import allure
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from framework.config import ANDROID_DEVICE_NAME, APP_PATH, APPIUM_SERVER
from framework.mobile.api_demos import HomeScreen


def _appium_is_running() -> bool:
    try:
        with urllib.request.urlopen(f"{APPIUM_SERVER}/status", timeout=3) as response:
            return response.status == 200
    except OSError:
        return False


def _not_ready(reason: str):
    """Skip locally, but fail in CI (REQUIRE_MOBILE=1) so a broken setup can't pass silently."""
    if os.getenv("REQUIRE_MOBILE") == "1":
        pytest.fail(reason)
    pytest.skip(reason)


@pytest.fixture(scope="session")
def appium_options() -> UiAutomator2Options:
    app = Path(APP_PATH).resolve()
    if not app.exists():
        _not_ready(f"APK not found at {app}. See apps/README.md.")
    if not _appium_is_running():
        _not_ready(f"Appium server not reachable at {APPIUM_SERVER}. Start it with `appium`.")

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = ANDROID_DEVICE_NAME
    options.app = str(app)
    options.auto_grant_permissions = True
    options.new_command_timeout = 120
    # CI emulators are slow on first install.
    options.set_capability("appium:uiautomator2ServerInstallTimeout", 120_000)
    options.set_capability("appium:adbExecTimeout", 60_000)
    return options


@pytest.fixture
def driver(appium_options, request):
    """A fresh app session per test, with a screenshot attached to Allure on failure."""
    drv = webdriver.Remote(APPIUM_SERVER, options=appium_options)
    yield drv
    report = getattr(request.node, "rep_call", None)
    if report and report.failed:
        allure.attach(
            drv.get_screenshot_as_png(),
            name="screenshot-on-failure",
            attachment_type=allure.attachment_type.PNG,
        )
    drv.quit()


@pytest.fixture
def home(driver) -> HomeScreen:
    return HomeScreen(driver)
