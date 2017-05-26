import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_quotas')

@click.option(
    "--deleted",
    help="Only return quota(s) that have been deleted",
    is_flag=True
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, deleted=False):
    """Get a list of quotas
    """
    return ctx.gi.quotas.get_quotas(deleted=deleted)
