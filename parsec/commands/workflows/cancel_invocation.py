import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('cancel_invocation')
@click.argument("workflow_id", type=str)
@click.argument("invocation_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, workflow_id, invocation_id):
    """Cancel the scheduling of a workflow.
    """
    return ctx.gi.workflows.cancel_invocation(workflow_id, invocation_id)
