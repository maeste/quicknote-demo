from click.testing import CliRunner

from quicknote.cli import main


def test_list_empty() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["list"])
    assert result.exit_code == 0, "list should succeed on empty store"


def test_search_no_results() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["search", "nonexistent-xyz"])
    assert result.exit_code == 0
    assert "No notes matching" in result.output, "should report no matches"
