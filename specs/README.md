# Test plans

Markdown test plans, one per feature. The **test-planner** agent writes them; the
**test-generator** agent turns them into `tests/web/test_<feature>.py`.

| Plan | Tests |
|---|---|
| [checkout.md](checkout.md) | [tests/web/test_checkout.py](../tests/web/test_checkout.py) |

Plans are reviewed by a human like any other code: they define *what* we test, so a wrong
expected result here becomes a wrong test later.
