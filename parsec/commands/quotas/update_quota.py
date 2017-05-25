import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('update_quota')
@click.argument("quota_id", type=str)

@click.option(
    "--name",
    help="Name for the new quota. This must be unique within a Galaxy instance.",
    type=str
)
@click.option(
    "--description",
    help="Quota description. If you supply this parameter, but not the name, an error will be thrown.",
    type=str
)
@click.option(
    "--amount",
    help="Quota size (E.g. ``10000MB``, ``99 gb``, ``0.2T``, ``unlimited``)",
    type=str
)
@click.option(
    "--operation",
    help="One of (``+``, ``-``, ``=``). If you wish to change this value, you must also provide the ``amount``, otherwise it will not take effect.",
    type=str
)
@click.option(
    "--default",
    help="Whether or not this is a default quota. Valid values are ``no``, ``unregistered``, ``registered``. Calling this method with ``default=\"no\"`` on a non-default quota will throw an error. Not passing this parameter is equivalent to passing ``no``.",
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
def cli(ctx, quota_id, name="", description="", amount="", operation="", default="no", in_users=None, in_groups=None):
    """Update an existing quota
    """
    return ctx.gi.quotas.update_quota(quota_id, name=name, description=description, amount=amount, operation=operation, default=default, in_users=in_users, in_groups=in_groups)
