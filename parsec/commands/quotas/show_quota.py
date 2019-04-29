import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('show_quota')
@click.argument("quota_id", type=str)
@click.option(
    "--deleted",
    help="Search for quota in list of ones already marked as deleted",
    is_flag=True
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, quota_id, deleted=False):
    """Display information on a quota

Output:

    A description of quota.
          For example::

            {u'bytes': 107374182400,
             u'default': [],
             u'description': u'just testing',
             u'display_amount': u'100.0 GB',
             u'groups': [],
             u'id': u'0604c8a56abe9a50',
             u'model_class': u'Quota',
             u'name': u'test ',
             u'operation': u'=',
             u'users': []}
    """
    return ctx.gi.quotas.show_quota(quota_id, deleted=deleted)
