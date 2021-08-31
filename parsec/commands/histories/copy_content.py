import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('copy_content')
@click.argument("history_id", type=str)
@click.argument("content_id", type=str)
@click.option(
    "--source",
    help="Source of the content to be copied: 'hda' (for a history dataset, the default), 'hdca' (for a dataset collection), 'library' (for a library dataset) or 'library_folder' (for all datasets in a library folder).",
    default="hda",
    show_default=True,
    type=str
)
@pass_context
@custom_exception
@json_output
def cli(ctx, history_id, content_id, source="hda"):
    """Copy existing content (e.g. a dataset) to a history.

Output:

    Information about the copied content
    """
    return ctx.gi.histories.copy_content(history_id, content_id, source=source)
