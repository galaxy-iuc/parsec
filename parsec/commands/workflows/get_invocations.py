import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_invocations')
@click.argument("workflow_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, workflow_id):
    """Get a list containing all the workflow invocations corresponding to the specified workflow.
    """
    return ctx.gi.workflows.get_invocations(workflow_id)
