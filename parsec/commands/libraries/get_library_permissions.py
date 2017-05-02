import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_library_permissions')
@click.argument("library_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, library_id):
    """Get the permessions for a library.
    """
    return ctx.gi.libraries.get_library_permissions(library_id)
