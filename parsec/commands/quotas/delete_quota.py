import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, str_output


@click.command('delete_quota')
@click.argument("quota_id", type=str)
@pass_context
@custom_exception
@str_output
def cli(ctx, quota_id):
    """Delete a quota

Output:

    A description of the changes, mentioning the deleted quota.
          For example::

            "Deleted 1 quotas: Testing-B"
    """
    return ctx.gi.quotas.delete_quota(quota_id)
