import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('undelete_quota')
@click.argument("quota_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, quota_id):
    """Undelete a quota
    """
    return ctx.gi.quotas.undelete_quota(quota_id)
