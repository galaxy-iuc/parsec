import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('create_quota')
@click.argument("name", type=str)
@click.argument("description", type=str)
@click.argument("amount", type=str)
@click.argument("operation", type=str)

@click.option(
    "--default",
    help="Whether or not this is a default quota. Valid values are ``no``, ``unregistered``, ``registered``. None is equivalent to ``no``.",
    default="no",
    type=str
)
@click.option(
    "--in_users",
    help="A list of user IDs or user emails.",
    type=str,
    multiple=True
)
@click.option(
    "--in_groups",
    help="A list of group IDs or names.",
    type=str,
    multiple=True
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, name, description, amount, operation, default="no", in_users=None, in_groups=None):
    """Create a new quota
    """
    return ctx.gi.quotas.create_quota(name, description, amount, operation, default=default, in_users=in_users, in_groups=in_groups)
