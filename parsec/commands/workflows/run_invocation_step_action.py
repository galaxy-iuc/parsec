import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('run_invocation_step_action')
@click.argument("workflow_id", type=str)
@click.argument("invocation_id", type=str)
@click.argument("step_id", type=str)
@click.argument("action")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, workflow_id, invocation_id, step_id, action):
    """nature of this action and what is expected will vary based on the the type of workflow step (the only currently valid action is True/False for pause steps).
    """
    return ctx.gi.workflows.run_invocation_step_action(workflow_id, invocation_id, step_id, action)
