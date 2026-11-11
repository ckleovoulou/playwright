import pytest


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Store each phase's report on the test item so fixtures can see if the test failed."""
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


def pytest_collection_modifyitems(items):
    """Auto-tag tests with `web` or `mobile` based on their folder."""
    for item in items:
        path = str(item.fspath)
        if "/tests/web/" in path.replace("\\", "/"):
            item.add_marker(pytest.mark.web)
        elif "/tests/mobile/" in path.replace("\\", "/"):
            item.add_marker(pytest.mark.mobile)
