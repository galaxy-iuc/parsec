import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('show_quota')
@click.argument("quota_id", type=str)
@click.option(
    "--deleted",
    help="Search for quota in list of ones already marked as deleted",
    is_flag=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, quota_id, deleted=False):
    """Display information on a quota

Output:

    A description of quota.
          For example::

            {'bytes': 107374182400,
             'default': [],
             'description': 'just testing',
             'display_amount': '100.0 GB',
             'groups': [],
             'id': '0604c8a56abe9a50',
             'model_class': 'Quota',
             'name': 'test ',
             'operation': '=',
             'users': []}
    """
    return ctx.gi.quotas.show_quota(quota_id, deleted=deleted)
