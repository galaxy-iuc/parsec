import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_workflows')
@click.option(
    "--workflow_id",
    help="Encoded workflow ID (incompatible with ``name``)",
    type=str
)
@click.option(
    "--name",
    help="Filter by name of workflow (incompatible with ``workflow_id``). If multiple names match the given name, all the workflows matching the argument will be returned.",
    type=str
)
@click.option(
    "--published",
    help="if ``True``, return also published workflows",
    is_flag=True
)
@pass_context
@custom_exception
@list_output
def cli(ctx, workflow_id="", name="", published=False):
    """Get all workflows or filter the specific one(s) via the provided ``name`` or ``workflow_id``. Provide only one argument, ``name`` or ``workflow_id``, but not both.

Output:

    A list of workflow dicts.
                 For example::

                   [{u'id': u'92c56938c2f9b315',
                     u'name': u'Simple',
                     u'url': u'/api/workflows/92c56938c2f9b315'}]
    """
    return ctx.gi.workflows.get_workflows(workflow_id=workflow_id, name=name, published=published)
