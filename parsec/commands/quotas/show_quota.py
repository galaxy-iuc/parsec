import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('show_quota')
@click.argument("quota_id", type=str)

@click.option(
    "--deleted",
    help="Search for quota in list of ones already marked as deleted",
    is_flag=True
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, quota_id, deleted=False):
    """Display information on a quota
    """
    return ctx.gi.quotas.show_quota(quota_id, deleted=deleted)
