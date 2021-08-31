import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_workflows')
@click.option(
    "--workflow_id",
    help="Encoded workflow ID",
    type=str
)
@click.option(
    "--name",
    help="Workflow name to filter on.",
    type=str
)
@click.option(
    "--published",
    help="if ``True``, return also published workflows",
    is_flag=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, workflow_id="", name="", published=False):
    """Get all workflows, or select a subset by specifying optional arguments for filtering (e.g. a workflow name).

Output:

    A list of workflow dicts.
                 For example::

                   [{'id': '92c56938c2f9b315',
                     'name': 'Simple',
                     'url': '/api/workflows/92c56938c2f9b315'}]
    """
    return ctx.gi.workflows.get_workflows(workflow_id=workflow_id, name=name, published=published)
