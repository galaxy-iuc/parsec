import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_quotas')
@click.option(
    "--deleted",
    help="Only return quota(s) that have been deleted",
    is_flag=True
)
@pass_context
@custom_exception
@list_output
def cli(ctx, deleted=False):
    """Get a list of quotas

Output:

    A list of dicts with details on individual quotas.
          For example::

            [{u'id': u'0604c8a56abe9a50',
              u'model_class': u'Quota',
              u'name': u'test ',
              u'url': u'/api/quotas/0604c8a56abe9a50'},
             {u'id': u'1ee267091d0190af',
              u'model_class': u'Quota',
              u'name': u'workshop',
              u'url': u'/api/quotas/1ee267091d0190af'}]
    """
    return ctx.gi.quotas.get_quotas(deleted=deleted)
