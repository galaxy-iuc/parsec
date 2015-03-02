import click

from parsec import options
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output

@click.command('quotas_show_quota')
@options.galaxy_instance()
@click.argument("quota_id", type=str)

@click.option(
    "--deleted",
    help="Search for quota in list of ones already marked as deleted",
    type=bool
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, galaxy_instance, quota_id, deleted=False):
    """Display information on a quota
    """
    return ctx.gi.quotas.show_quota(quota_id, deleted=deleted)
