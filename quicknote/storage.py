import json
import os
from datetime import datetime
from pathlib import Path


DEFAULT_STORE = Path.home() / ".quicknote" / "notes.json"


def _ensure_store(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text("[]")


def load_notes(path=None):
    path = Path(path) if path else DEFAULT_STORE
    _ensure_store(path)
    with open(path) as f:
        return json.load(f)


def save_notes(notes, path=None):
    path = Path(path) if path else DEFAULT_STORE
    _ensure_store(path)
    with open(path, "w") as f:
        json.dump(notes, f, indent=2)


def add_note(title, body, tags=None, path=None):
    notes = load_notes(path)
    note = {
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


def delete_note(note_id, path=None):
    notes = load_notes(path)
    notes = [n for n in notes if n["id"] != note_id]
    save_notes(notes, path)


def search_notes(query, path=None):
    notes = load_notes(path)
    query = query.lower()
    results = []
    for note in notes:
        if query in note["title"].lower() or query in note["body"].lower():
            results.append(note)
        elif any(query in t.lower() for t in note.get("tags", [])):
            results.append(note)
    return results


def get_note(note_id, path=None):
    notes = load_notes(path)
    for note in notes:
        if note["id"] == note_id:
            return note
    return None


def update_note(note_id, title=None, body=None, tags=None, path=None):
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
