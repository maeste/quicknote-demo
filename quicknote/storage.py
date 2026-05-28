import json
from datetime import datetime
from pathlib import Path
from typing import Any

Note = dict[str, Any]

DEFAULT_STORE = Path.home() / ".quicknote" / "notes.json"


def _ensure_store(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text("[]")


def _resolve(path: str | Path | None) -> Path:
    return Path(path) if path else DEFAULT_STORE


def load_notes(path: str | Path | None = None) -> list[Note]:
    store = _resolve(path)
    _ensure_store(store)
    with open(store) as f:
        return json.load(f)


def save_notes(notes: list[Note], path: str | Path | None = None) -> None:
    store = _resolve(path)
    _ensure_store(store)
    with open(store, "w") as f:
        json.dump(notes, f, indent=2)


def add_note(
    title: str, body: str, tags: list[str] | None = None, path: str | Path | None = None
) -> Note:
    notes = load_notes(path)
    note: Note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "tags": tags or [],
        "created": datetime.now().isoformat(),
        "updated": datetime.now().isoformat(),
    }
    notes.append(note)
    save_notes(notes, path)
    return note


def delete_note(note_id: int, path: str | Path | None = None) -> None:
    notes = load_notes(path)
    notes = [n for n in notes if n["id"] != note_id]
    save_notes(notes, path)


def search_notes(query: str, path: str | Path | None = None) -> list[Note]:
    notes = load_notes(path)
    query = query.lower()
    results: list[Note] = []
    for note in notes:
        if query in note["title"].lower() or query in note["body"].lower():
            results.append(note)
        elif any(query in t.lower() for t in note.get("tags", [])):
            results.append(note)
    return results


def get_note(note_id: int, path: str | Path | None = None) -> Note | None:
    notes = load_notes(path)
    for note in notes:
        if note["id"] == note_id:
            return note
    return None


def update_note(
    note_id: int,
    title: str | None = None,
    body: str | None = None,
    tags: list[str] | None = None,
    path: str | Path | None = None,
) -> Note | None:
    notes = load_notes(path)
    for note in notes:
        if note["id"] == note_id:
            if title is not None:
                note["title"] = title
            if body is not None:
                note["body"] = body
            if tags is not None:
                note["tags"] = tags
            note["updated"] = datetime.now().isoformat()
            save_notes(notes, path)
            return note
    return None
