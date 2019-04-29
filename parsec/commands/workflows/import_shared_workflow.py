import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('import_shared_workflow')
@click.argument("workflow_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, workflow_id):
    """Imports a new workflow from the shared published workflows.

Output:

    A description of the workflow.
          For example::

            {u'id': u'ee0e2b4b696d9092',
             u'model_class': u'StoredWorkflow',
             u'name': u'Super workflow that solves everything!',
             u'published': False,
             u'tags': [],
             u'url': u'/api/workflows/ee0e2b4b696d9092'}
    """
    return ctx.gi.workflows.import_shared_workflow(workflow_id)
