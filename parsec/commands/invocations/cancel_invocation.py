import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('cancel_invocation')
@click.argument("invocation_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, invocation_id):
    """Cancel the scheduling of a workflow.

Output:

    The workflow invocation being cancelled
    """
    return ctx.gi.invocations.cancel_invocation(invocation_id)
