from pathlib import Path

from quicknote.storage import (
    add_note,
    delete_note,
    get_note,
    load_notes,
    search_notes,
    update_note,
)


def test_add_and_load(tmp_store: Path) -> None:
    note = add_note("Test", "Body text", tags=["demo"], path=tmp_store)
    assert note["id"] == 1, "first note should get id 1"
    assert note["title"] == "Test"

    notes = load_notes(tmp_store)
    assert len(notes) == 1, "exactly one note should be stored"


def test_delete(tmp_store: Path) -> None:
    add_note("Keep", "keep me", path=tmp_store)
    add_note("Remove", "delete me", path=tmp_store)
    delete_note(2, path=tmp_store)

    notes = load_notes(tmp_store)
    assert len(notes) == 1, "one note should remain after deleting id 2"
    assert notes[0]["title"] == "Keep"


def test_search_by_title(tmp_store: Path) -> None:
    add_note("Python Tips", "some tips", path=tmp_store)
    add_note("Rust Guide", "some guide", path=tmp_store)

    results = search_notes("python", path=tmp_store)
    assert len(results) == 1, "search should match exactly one title"
    assert results[0]["title"] == "Python Tips"


def test_search_by_tag(tmp_store: Path) -> None:
    add_note("Tagged", "body", tags=["workshop"], path=tmp_store)
    add_note("Untagged", "body", path=tmp_store)

    results = search_notes("workshop", path=tmp_store)
    assert len(results) == 1, "search should match the tagged note"


def test_get_note(tmp_store: Path) -> None:
    add_note("First", "body", path=tmp_store)
    note = get_note(1, path=tmp_store)
    assert note is not None, "note 1 should exist"
    assert note["title"] == "First"
    assert get_note(999, path=tmp_store) is None, "missing id should return None"


def test_update_note(tmp_store: Path) -> None:
    add_note("Original", "original body", path=tmp_store)
    updated = update_note(1, title="Updated", path=tmp_store)
    assert updated is not None
    assert updated["title"] == "Updated"
    assert updated["body"] == "original body", "body should be unchanged"


def test_empty_store(tmp_store: Path) -> None:
    assert load_notes(tmp_store) == [], "fresh store should be empty"
