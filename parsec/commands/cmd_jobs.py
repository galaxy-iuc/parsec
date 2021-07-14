import click
from parsec.commands.jobs.cancel_job import cli as cancel_job
from parsec.commands.jobs.get_common_problems import cli as get_common_problems
from parsec.commands.jobs.get_destination_params import cli as get_destination_params
from parsec.commands.jobs.get_inputs import cli as get_inputs
from parsec.commands.jobs.get_jobs import cli as get_jobs
from parsec.commands.jobs.get_metrics import cli as get_metrics
from parsec.commands.jobs.get_outputs import cli as get_outputs
from parsec.commands.jobs.get_state import cli as get_state
from parsec.commands.jobs.report_error import cli as report_error
from parsec.commands.jobs.rerun_job import cli as rerun_job
from parsec.commands.jobs.resume_job import cli as resume_job
from parsec.commands.jobs.search_jobs import cli as search_jobs
from parsec.commands.jobs.show_job import cli as show_job
from parsec.commands.jobs.show_job_lock import cli as show_job_lock
from parsec.commands.jobs.update_job_lock import cli as update_job_lock
from parsec.commands.jobs.wait_for_job import cli as wait_for_job


@click.group()
def cli():
    pass


cli.add_command(cancel_job)
cli.add_command(get_common_problems)
cli.add_command(get_destination_params)
cli.add_command(get_inputs)
cli.add_command(get_jobs)
cli.add_command(get_metrics)
cli.add_command(get_outputs)
cli.add_command(get_state)
cli.add_command(report_error)
cli.add_command(rerun_job)
cli.add_command(resume_job)
cli.add_command(search_jobs)
cli.add_command(show_job)
cli.add_command(show_job_lock)
cli.add_command(update_job_lock)
cli.add_command(wait_for_job)
