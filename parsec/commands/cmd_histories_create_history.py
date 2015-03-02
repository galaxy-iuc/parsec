import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('histories_create_history')
@options.galaxy_instance()
@click.argument("name", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, name):
    """Create a new history, optionally setting the ``name``.
    """
    return ctx.gi.histories.create_history(name)
