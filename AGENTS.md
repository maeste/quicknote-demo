# AGENTS.md — QuickNote

> Portable, vendor-neutral instructions for any AI coding agent (Claude Code,
> Codex, opencode, pi, …). `CLAUDE.md` is a symlink to this file.

## What this project is

QuickNote is a small CLI note manager in Python. Users add, list, search,
edit, and delete plain-text notes stored as JSON on the local filesystem.
Keep it small — no servers, no database.

## Where things live

```
quicknote/        application source
  cli.py          Click-based CLI entry point
  storage.py      JSON file read/write operations
  __init__.py     package version
```

## Build · test · lint

```bash
pip install -e ".[dev]"   # install with dev deps
pytest                    # run tests
ruff check .              # lint
ruff format .             # format
```

## Conventions

- Imports: absolute, stdlib first, then third-party, then local.
- Strings: double quotes. Type hints on public functions.
- Naming: `snake_case` functions/vars, `PascalCase` classes.
- All note persistence goes through `storage.py` — never direct file I/O elsewhere.

## Pitfalls

- Don't hardcode the notes file path — use `storage.py` functions, which take an
  optional `path` parameter.
- `id` is a simple incrementing integer, not a UUID. Don't assume cross-reset uniqueness.
- Don't add heavy dependencies — this is a lightweight CLI.

## Safe to run

These commands are read-only or test-scoped and safe for an agent to run
unattended: `pytest`, `ruff check .`, `ruff format --check .`, `git status`,
`git diff`. See `docs/agent-execution.md` for the sandbox/execution policy.
