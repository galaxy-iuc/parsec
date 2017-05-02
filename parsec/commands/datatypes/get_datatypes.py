import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('datatypes_get_datatypes')
@click.option(
    "--extension_only",
    help="None"
)
@click.option(
    "--upload_only",
    help="None"
)
@pass_context
@bioblend_exception
@dict_output
def cli(ctx, extension_only=False, upload_only=False):
    """Displays a collection (list) of datatypes.
    """
    return ctx.gi.datatypes.get_datatypes(
        extension_only=extension_only,
        upload_only=upload_only)
