import click
from parsec.commands.invocations.cancel_invocation import cli as cancel_invocation
from parsec.commands.invocations.get_invocation_biocompute_object import cli as get_invocation_biocompute_object
from parsec.commands.invocations.get_invocation_report import cli as get_invocation_report
from parsec.commands.invocations.get_invocation_report_pdf import cli as get_invocation_report_pdf
from parsec.commands.invocations.get_invocation_step_jobs_summary import cli as get_invocation_step_jobs_summary
from parsec.commands.invocations.get_invocation_summary import cli as get_invocation_summary
from parsec.commands.invocations.get_invocations import cli as get_invocations
from parsec.commands.invocations.rerun_invocation import cli as rerun_invocation
from parsec.commands.invocations.run_invocation_step_action import cli as run_invocation_step_action
from parsec.commands.invocations.show_invocation import cli as show_invocation
from parsec.commands.invocations.show_invocation_step import cli as show_invocation_step
from parsec.commands.invocations.wait_for_invocation import cli as wait_for_invocation


@click.group()
def cli():
    pass


cli.add_command(cancel_invocation)
cli.add_command(get_invocation_biocompute_object)
cli.add_command(get_invocation_report)
cli.add_command(get_invocation_report_pdf)
cli.add_command(get_invocation_step_jobs_summary)
cli.add_command(get_invocation_summary)
cli.add_command(get_invocations)
cli.add_command(rerun_invocation)
cli.add_command(run_invocation_step_action)
cli.add_command(show_invocation)
cli.add_command(show_invocation_step)
cli.add_command(wait_for_invocation)
