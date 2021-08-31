import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('import_shared_workflow')
@click.argument("workflow_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, workflow_id):
    """Imports a new workflow from the shared published workflows.

Output:

    A description of the workflow.
          For example::

            {'id': 'ee0e2b4b696d9092',
             'model_class': 'StoredWorkflow',
             'name': 'Super workflow that solves everything!',
             'published': False,
             'tags': [],
             'url': '/api/workflows/ee0e2b4b696d9092'}
    """
    return ctx.gi.workflows.import_shared_workflow(workflow_id)
