import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('wait_for_invocation')
@click.argument("invocation_id", type=str)
@click.option(
    "--maxwait",
    help="Total time (in seconds) to wait for the invocation state to become terminal. If the invocation state is not terminal within this time, a ``TimeoutException`` will be raised.",
    default="12000",
    show_default=True,
    type=float
)
@click.option(
    "--interval",
    help="Time (in seconds) to wait between 2 consecutive checks.",
    default="3",
    show_default=True,
    type=float
)
@click.option(
    "--check",
    help="Whether to check if the invocation terminal state is 'scheduled'.",
    default="True",
    show_default=True,
    is_flag=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, invocation_id, maxwait=12000, interval=3, check=True):
    """Wait until an invocation is in a terminal state.

Output:

    Details of the workflow invocation.
    """
    return ctx.gi.invocations.wait_for_invocation(invocation_id, maxwait=maxwait, interval=interval, check=check)
