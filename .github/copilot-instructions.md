# Copilot instructions

Follow `AGENTS.md` in the repository root for project layout, locator strategy and coding standards.

Short version:
- Python, Playwright (sync API) + Pytest, Page Object Model in `framework/pages/`.
- Locators: role → label/placeholder → `get_by_test_id` (`data-test`) → CSS class. No XPath.
- Assert in tests with `expect(...)`. No `time.sleep()` or `wait_for_timeout()`.
- Test data in `framework/data.py`. Tag tests `smoke` or `regression` and add `@allure.title`.
- Never weaken an assertion to make a test pass.

Custom agents for this repo are in `.github/agents/`: `test-planner`, `test-generator`, `test-healer`.
