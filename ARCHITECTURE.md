# Architecture — QuickNote

## Overview

QuickNote is a single-user CLI application. No server, no database — just
JSON files on the local filesystem.

```
User → CLI (Click) → Storage (JSON) → ~/.quicknote/notes.json
```

## Modules

### `quicknote/cli.py`
Click command definitions. Each command maps to one storage operation. No
business logic here — it translates CLI arguments into function calls and
formats output.

### `quicknote/storage.py`
Pure data-access layer. All functions accept an optional `path` parameter to
override the default store location (used by tests).

## Data model

Each note is a JSON object:
```json
{ "id": 1, "title": "string", "body": "string",
  "tags": ["string"], "created": "ISO-8601", "updated": "ISO-8601" }
```

The store file is a JSON array of note objects.

## Design decisions

- **JSON over SQLite**: simplicity, human-readable, easy to back up/sync.
- **Click over argparse**: better UX (help formatting, confirmation prompts).
- **Dicts over dataclasses for notes**: the model is simple enough.

See `docs/adr/` for recorded decisions.
