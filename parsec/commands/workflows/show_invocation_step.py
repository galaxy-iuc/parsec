import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('show_invocation_step')
@click.argument("workflow_id", type=str)
@click.argument("invocation_id", type=str)
@click.argument("step_id", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, workflow_id, invocation_id, step_id):
    """See the details of a particular workflow invocation step.
    """
    return ctx.gi.workflows.show_invocation_step(workflow_id, invocation_id, step_id)
