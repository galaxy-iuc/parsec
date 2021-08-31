import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('run_invocation_step_action')
@click.argument("workflow_id", type=str, help="Encoded workflow ID")
@click.argument("invocation_id", type=str, help="Encoded workflow invocation ID")
@click.argument("step_id", type=str, help="Encoded workflow invocation step ID")
@click.argument("action", type=str, help="Action to use when updating state, semantics depends on step type.")
@pass_context
@custom_exception
@json_output
def cli(ctx, workflow_id, invocation_id, step_id, action):
    """nature of this action and what is expected will vary based on the the type of workflow step (the only currently valid action is True/False for pause steps).

Output:

    Representation of the workflow invocation step
    """
    return ctx.gi.workflows.run_invocation_step_action(workflow_id, invocation_id, step_id, action)
