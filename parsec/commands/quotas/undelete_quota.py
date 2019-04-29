import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, str_output


@click.command('undelete_quota')
@click.argument("quota_id", type=str)
@pass_context
@custom_exception
@str_output
def cli(ctx, quota_id):
    """Undelete a quota

Output:

    A description of the changes, mentioning the undeleted quota.
          For example::

            "Undeleted 1 quotas: Testing-B"
    """
    return ctx.gi.quotas.undelete_quota(quota_id)
