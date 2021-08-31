import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_invocation_summary')
@click.argument("invocation_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, invocation_id):
    """Get a summary of an invocation, stating the number of jobs which succeed, which are paused and which have errored.

Output:

    The invocation summary.
          For example::

            {'states': {'paused': 4, 'error': 2, 'ok': 2},
             'model': 'WorkflowInvocation',
             'id': 'a799d38679e985db',
             'populated_state': 'ok'}
    """
    return ctx.gi.invocations.get_invocation_summary(invocation_id)
