import time
import click
import json
from parsec.cli import pass_context
from parsec.decorators import bioblend_exception
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

@pass_context
@bioblend_exception
def cli(ctx, workflow_id, invocation_id, exit_early=False, backoff_min=1, backoff_max=60):
    """Given a workflow and invocation id, wait until that invocation is
    complete (or one or more steps have errored)

    This will exit with the following error codes:

    - 0: done successfully
    - 1: running (if --exit_early)
    - 2: failure
    - 3: unknown
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
            ctx.vlog("Checking workflow %s states: %s", workflow_id, state_rep)

            if exit_early:
                print(json.dumps({'state': 'running', 'job_states': states}))
                ctx.exit(1)

            # Conditions which must be true for all jobs before we can be done
            if all([state == 'ok' for state in states]):
                print(json.dumps({'state': 'done', 'job_states': states}))
                ctx.exit(0)

            # Conditions on which to exit immediately (i.e. due to a failure)
            if any([state in ('error', 'paused') for state in states]):
                print(json.dumps({'state': 'failure', 'job_states': states}))
                ctx.exit(2)
        else:
            ctx.vlog("Waiting for invocation to be scheduled")

            if exit_early:
                print(json.dumps({'state': 'unscheduled'}))
                ctx.exit(0)

        time.sleep(backoff.duration())
    ctx.exit(3)
