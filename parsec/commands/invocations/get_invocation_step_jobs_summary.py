import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_invocation_step_jobs_summary')
@click.argument("invocation_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, invocation_id):
    """Get a detailed summary of an invocation, listing all jobs with their job IDs and current states.

Output:

    The invocation step jobs summary.
          For example::

            [{'id': 'e85a3be143d5905b',
              'model': 'Job',
              'populated_state': 'ok',
              'states': {'ok': 1}},
             {'id': 'c9468fdb6dc5c5f1',
              'model': 'Job',
              'populated_state': 'ok',
              'states': {'running': 1}},
             {'id': '2a56795cad3c7db3',
              'model': 'Job',
              'populated_state': 'ok',
              'states': {'new': 1}}]
    """
    return ctx.gi.invocations.get_invocation_step_jobs_summary(invocation_id)
