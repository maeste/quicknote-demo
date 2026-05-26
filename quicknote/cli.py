import click

from quicknote.storage import (
    add_note,
    delete_note,
    get_note,
    load_notes,
    search_notes,
    update_note,
)


@click.group()
@click.version_option()
def main():
    """QuickNote - Manage your notes from the terminal."""
    pass


@main.command()
@click.argument("title")
@click.option("-b", "--body", default="", help="Note body text")
@click.option("-t", "--tag", multiple=True, help="Tags for the note")
def add(title, body, tag):
    """Add a new note."""
    note = add_note(title, body, tags=list(tag))
    click.echo(f"Created note #{note['id']}: {note['title']}")


@main.command("list")
@click.option("--tag", help="Filter by tag")
def list_notes(tag):
    """List all notes."""
    notes = load_notes()
    if tag:
        notes = [n for n in notes if tag.lower() in [t.lower() for t in n.get("tags", [])]]

    if not notes:
        click.echo("No notes found.")
        return

    for note in notes:
        tags_str = ", ".join(note.get("tags", []))
        tag_display = f" [{tags_str}]" if tags_str else ""
        click.echo(f"  #{note['id']}  {note['title']}{tag_display}")


@main.command()
@click.argument("query")
def search(query):
    """Search notes by title, body, or tags."""
    results = search_notes(query)
    if not results:
        click.echo(f"No notes matching '{query}'.")
        return

    click.echo(f"Found {len(results)} note(s):")
    for note in results:
        click.echo(f"  #{note['id']}  {note['title']}")


@main.command()
@click.argument("note_id", type=int)
def show(note_id):
    """Show a single note."""
    note = get_note(note_id)
    if not note:
        click.echo(f"Note #{note_id} not found.")
        return

    click.echo(f"#{note['id']}  {note['title']}")
    click.echo(f"Created: {note['created']}")
    if note.get("tags"):
        click.echo(f"Tags: {', '.join(note['tags'])}")
    click.echo()
    click.echo(note.get("body", ""))


@main.command()
@click.argument("note_id", type=int)
@click.confirmation_option(prompt="Are you sure you want to delete this note?")
def delete(note_id):
    """Delete a note by ID."""
    delete_note(note_id)
    click.echo(f"Deleted note #{note_id}.")


@main.command()
@click.argument("note_id", type=int)
@click.option("--title", help="New title")
@click.option("--body", help="New body")
@click.option("-t", "--tag", multiple=True, help="Replace tags")
def edit(note_id, title, body, tag):
    """Edit an existing note."""
    tags = list(tag) if tag else None
    note = update_note(note_id, title=title, body=body, tags=tags)
    if not note:
        click.echo(f"Note #{note_id} not found.")
        return
    click.echo(f"Updated note #{note['id']}: {note['title']}")


if __name__ == "__main__":
    main()
