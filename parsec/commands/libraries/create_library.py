import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('create_library')
@click.argument("name", type=str)
@click.option(
    "--description",
    help="Optional data library description",
    type=str
)
@click.option(
    "--synopsis",
    help="Optional data library synopsis",
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, name, description="", synopsis=""):
    """Create a data library with the properties defined in the arguments.

Output:

    Details of the created library.
          For example::

            {'id': 'f740ab636b360a70',
             'name': 'Library from bioblend',
             'url': '/api/libraries/f740ab636b360a70'}
    """
    return ctx.gi.libraries.create_library(name, description=description, synopsis=synopsis)
