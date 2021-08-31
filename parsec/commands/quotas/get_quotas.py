import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_quotas')
@click.option(
    "--deleted",
    help="Only return quota(s) that have been deleted",
    is_flag=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, deleted=False):
    """Get a list of quotas

Output:

    A list of dicts with details on individual quotas.
          For example::

            [{'id': '0604c8a56abe9a50',
              'model_class': 'Quota',
              'name': 'test ',
              'url': '/api/quotas/0604c8a56abe9a50'},
             {'id': '1ee267091d0190af',
              'model_class': 'Quota',
              'name': 'workshop',
              'url': '/api/quotas/1ee267091d0190af'}]
    """
    return ctx.gi.quotas.get_quotas(deleted=deleted)
