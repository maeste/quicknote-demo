# QuickNote

A simple CLI note manager built with Python and Click. Store, search, and
organize plain-text notes from your terminal.

## Quick Start

```bash
pip install -e .
quicknote add "My first note" --body "Hello world" --tag personal
quicknote list
quicknote search "hello"
```

## Installation

Requires Python 3.11+.

```bash
git clone <repo-url>
cd quicknote
pip install -e .
```

## Usage

| Command | Description |
|---------|-------------|
| `quicknote add "title"` | Create a new note |
| `quicknote list` | Show all notes |
| `quicknote list --tag work` | Filter by tag |
| `quicknote search "query"` | Search title, body, tags |
| `quicknote show <id>` | Display a single note |
| `quicknote edit <id>` | Modify title, body, or tags |
| `quicknote delete <id>` | Remove a note |

Notes are stored as JSON in `~/.quicknote/notes.json`.

## For AI agents

This project is agent-ready. See [`AGENTS.md`](AGENTS.md) for instructions,
conventions, and the safe-to-run command list.

## License

MIT
