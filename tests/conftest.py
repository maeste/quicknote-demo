from pathlib import Path

import pytest


@pytest.fixture
def tmp_store(tmp_path: Path) -> Path:
    """Provide a temporary notes store file."""
    return tmp_path / "notes.json"
