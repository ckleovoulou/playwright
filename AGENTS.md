# Agent rules for this repository

These rules apply to every AI agent working here (GitHub Copilot, Claude Code, or any other)
and to humans. The planner, generator and healer agents in `.github/agents/` and
`.claude/agents/` all follow this file.

## Project

- Python test automation framework: **Playwright + Pytest** (web) and **Appium** (Android).
- System under test (web): https://www.saucedemo.com — demo users are listed on its login page.
- System under test (mobile): Appium's `ApiDemos-debug.apk`.
- Reports: Allure (`allure-results/`).

## Commands

```bash
pip install -r requirements.txt && playwright install chromium   # setup
pytest tests/web                                                  # all web tests
pytest tests/web -m smoke                                         # smoke only
pytest tests/web/test_login.py --headed                           # watch one file run
pytest tests/mobile                                               # needs Appium + emulator
ruff check . && ruff format --check .                             # lint
```

## Folder layout

| Path | Contents |
|---|---|
| `specs/` | Markdown test plans written by the planner agent |
| `framework/pages/` | Page objects (one class per page) |
| `framework/mobile/` | Screen objects for the Android app |
| `framework/data.py` | Test data (products, customers, expected messages) |
| `framework/config.py` | Users, URLs and env-driven settings |
| `tests/web/` | Web tests, one file per feature: `test_<feature>.py` |
| `tests/mobile/` | Appium smoke tests |

## Locator strategy (in priority order)

1. `get_by_role(role, name=...)` — buttons, links, headings, checkboxes.
2. `get_by_label(...)` / `get_by_placeholder(...)` — form fields.
3. `get_by_test_id(...)` — this project maps it to the `data-test` attribute.
4. CSS class — only when 1–3 are not available. Never XPath. Never `nth()` on generic selectors.

Always confirm a locator against the live page (Playwright MCP `browser_snapshot`) before using it.

## Coding standards

- **Page objects** expose locators (as `@property`) and actions. **No assertions** in page objects.
- **Tests** assert with Playwright's `expect(...)` (auto-waiting). Plain `assert` only for computed
  values such as sorted lists.
- **No fixed waits**: never `time.sleep()` or `page.wait_for_timeout()`.
- **Test data** goes in `framework/data.py`, not inline in tests.
- One behaviour per test. Name tests after the behaviour: `test_checkout_requires_postal_code`.
- Tag every test with `@pytest.mark.smoke` or `@pytest.mark.regression`, and give it an
  `@allure.title(...)`. Set `pytestmark = allure.feature("<Feature>")` per file.
- Wrap page-object actions in `allure.step(...)` so reports read like test steps.
- Reuse fixtures from `tests/web/conftest.py` (`login_page`, `inventory`) instead of logging in by hand.
- Code must pass `ruff check .`.

## What agents must never do

- Delete or weaken an assertion to make a test pass.
- Hide a real product bug. If the app is wrong, mark the test
  `@pytest.mark.xfail(reason="BUG: <what is wrong>", strict=True)` and say so in the summary.
- Add dependencies without being asked.
- Commit. A human reviews every generated test before it is merged.

## Human review checklist (before merge)

- [ ] The test checks the behaviour described in the spec, not just that the page loads.
- [ ] Locators follow the priority above and work in headed mode.
- [ ] No duplicated page-object code; new actions were added to the right page class.
- [ ] Runs green 3 times in a row (no flakiness): `for i in 1 2 3; do pytest <file> || break; done`.
