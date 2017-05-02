import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('show_invocation')
@click.argument("workflow_id", type=str)
@click.argument("invocation_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, workflow_id, invocation_id):
    """Get a workflow invocation object representing the scheduling of a workflow. This object may be sparse at first (missing inputs and invocation steps) and will become more populated as the workflow is actually scheduled.
    """
    return ctx.gi.workflows.show_invocation(workflow_id, invocation_id)
