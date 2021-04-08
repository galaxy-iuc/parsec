import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('import_history')
@click.option(
    "--file_path",
    help="Path to exported history archive on disk. :type url: str :param url: URL for an exported history archive",
    type=str
)
@click.option(
    "--url",
    help=""
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, file_path="", url=""):
    """Import a history from an archive on disk or a URL.

Output:

    
    """
    return ctx.gi.histories.import_history(file_path=file_path, url=url)
