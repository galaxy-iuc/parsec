import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_datatypes')

@click.option(
    "--extension_only",
    help=""
)
@click.option(
    "--upload_only",
    help=""
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, extension_only=False, upload_only=False):
    """Get the list of all installed datatypes.
    """
    return ctx.gi.datatypes.get_datatypes(extension_only=extension_only, upload_only=upload_only)
