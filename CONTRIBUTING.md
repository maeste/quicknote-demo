# Contributing to QuickNote

## Setup

```bash
git clone <repo-url>
cd quicknote
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Making changes

1. Create a branch: `git checkout -b feat/short-description`
2. Make your changes
3. Run tests: `pytest`
4. Run linter: `ruff check .`
5. Open a pull request against `main`

## Conventions

- Commit messages in imperative mood ("add feature", not "added feature")
- Keep PRs small and focused
- Update `AGENTS.md` if you change project structure or conventions
