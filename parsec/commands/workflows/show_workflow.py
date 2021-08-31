import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('show_workflow')
@click.argument("workflow_id", type=str)
@click.option(
    "--version",
    help="Workflow version to show",
    type=int
)
@pass_context
@custom_exception
@json_output
def cli(ctx, workflow_id, version=""):
    """Display information needed to run a workflow.

Output:

    A description of the workflow and its inputs.
          For example::

            {'id': '92c56938c2f9b315',
             'inputs': {'23': {'label': 'Input Dataset', 'value': ''}},
             'name': 'Simple',
             'url': '/api/workflows/92c56938c2f9b315'}
    """
    return ctx.gi.workflows.show_workflow(workflow_id, version=version)
