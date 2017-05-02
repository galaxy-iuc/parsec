import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('show_user')
@click.argument("user_id", type=str)

@click.option(
    "--deleted",
    help="whether to return results for a deleted user",
    is_flag=True
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, user_id, deleted=False):
    """Display information about a user.
    """
    return ctx.gi.users.show_user(user_id, deleted=deleted)
