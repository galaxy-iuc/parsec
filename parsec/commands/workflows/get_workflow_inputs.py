import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_workflow_inputs')
@click.argument("workflow_id", type=str)
@click.argument("label", type=str)
@pass_context
@custom_exception
@list_output
def cli(ctx, workflow_id, label):
    """Get a list of workflow input IDs that match the given label. If no input matches the given label, an empty list is returned.

Output:

    list of workflow inputs matching the label query
    """
    return ctx.gi.workflows.get_workflow_inputs(workflow_id, label)
