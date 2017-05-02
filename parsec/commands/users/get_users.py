import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_users')

@click.option(
    "--deleted",
    help="None"
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, deleted=False):
    """Get a list of all registered users. If ``deleted`` is set to ``True``, get a list of deleted users.
    """
    return ctx.gi.users.get_users(deleted=deleted)
