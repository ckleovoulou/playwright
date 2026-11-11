import allure
import pytest

pytestmark = [allure.feature("Mobile smoke (Android)"), pytest.mark.smoke]


@allure.title("App launches on the home list with the main API categories")
def test_home_screen_lists_categories(home):
    for name in ("App", "Views", "Text"):
        assert home.category(name).is_displayed(), f"'{name}' should be visible on the home screen"


@allure.title("Opening 'Views' shows the list of view demos")
def test_open_views_section(home):
    views = home.open_views()

    assert views.by_accessibility_id("Animation").is_displayed()


@allure.title("Text typed into a form field is kept")
def test_type_into_text_field(home):
    controls = home.open_views().open_controls_light_theme()
    controls.type_text("Hello Appium")

    assert controls.text_field.text == "Hello Appium"
