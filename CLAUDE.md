@AGENTS.md

## Claude Code notes

- The Playwright MCP server is configured in `.mcp.json`; its tools are named `mcp__playwright__browser_*`.
- The three subagents live in `.claude/agents/`: `test-planner`, `test-generator`, `test-healer`.
  Run them in that order: plan → generate → heal.
