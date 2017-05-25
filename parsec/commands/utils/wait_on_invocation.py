import time
import click
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output
from justbackoff import Backoff


@click.command('wait_on_invocation')
@click.argument("workflow_id", type=str, required=True)
@click.argument("invocation_id", type=str, required=True)
@click.option(
    "--exit_early",
    help="Exit immediately after checking status rather than sleeping indefinitely",
    is_flag=True
)
@click.option(
    "--backoff_min",
    help="Minimum time to sleep between checks, in seconds.",
    default=1,
    type=float,
)
@click.option(
    "--backoff_max",
    help="Maximum time to sleep between checks, in seconds",
    default=60,
    type=float,
)
@click.option('-v', '--verbose', count=True)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, workflow_id, invocation_id, verbose, exit_early=False, backoff_min=1, backoff_max=60):
    """Given a workflow and invocation id, wait until that invocation is
    complete (or one or more steps have errored)
    """
    backoff = Backoff(min_ms=backoff_min * 1000, max_ms=backoff_max * 1000, factor=2, jitter=True)

    prev_state = None
    while True:
        # Fetch the current state
        latest_state = ctx.gi.workflows.show_invocation(workflow_id, invocation_id)
        # Get step states
        states = [step['state'] for step in latest_state['steps'] if step['state'] is not None and step['state'] != 'deleted']
        # Get a str based state representation
        state_rep = '|'.join(map(str, states))

        if state_rep != prev_state:
            backoff.reset()
        prev_state = state_rep

        # If it's scheduled, then let's look at steps. Otherwise steps probably don't exist yet.
        if latest_state['state'] == 'scheduled':
            if verbose > 1:
                click.echo("Checking workflow %s states: %s" % (workflow_id, state_rep))
            elif verbose > 0:
                click.echo('.', nl=False)

            if exit_early:
                if verbose > 0:
                    return {'state': 'running', 'job_states': states}

            # Conditions which must be true for all jobs before we can be done
            if all([state == 'ok' for state in states]):
                return {'state': 'done', 'job_states': states}

            # Conditions on which to exit immediately (i.e. due to a failure)
            if any([state in ('error', 'paused') for state in states]):
                return {'state': 'failure', 'job_states': states}
        else:
            if verbose > 1:
                click.echo("Waiting for invocation to be scheduled")
            elif verbose > 0:
                click.echo("+", nl=False)

            if exit_early:
                if verbose > 0:
                    return {'state': 'unscheduled'}

        time.sleep(backoff.duration())