import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('show_workflow')
@click.argument("workflow_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, workflow_id):
    """Display information needed to run a workflow.

Output:

    A description of the workflow and its inputs.
          For example::

            {u'id': u'92c56938c2f9b315',
             u'inputs': {u'23': {u'label': u'Input Dataset', u'value': u''}},
             u'name': u'Simple',
             u'url': u'/api/workflows/92c56938c2f9b315'}
    """
    return ctx.gi.workflows.show_workflow(workflow_id)
