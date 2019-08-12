import click
from parsec.commands.workflows.cancel_invocation import cli as cancel_invocation
from parsec.commands.workflows.delete_workflow import cli as delete_workflow
from parsec.commands.workflows.export_workflow_dict import cli as export_workflow_dict
from parsec.commands.workflows.export_workflow_to_local_path import cli as export_workflow_to_local_path
from parsec.commands.workflows.get_invocations import cli as get_invocations
from parsec.commands.workflows.get_workflow_inputs import cli as get_workflow_inputs
from parsec.commands.workflows.get_workflows import cli as get_workflows
from parsec.commands.workflows.import_shared_workflow import cli as import_shared_workflow
from parsec.commands.workflows.import_workflow_dict import cli as import_workflow_dict
from parsec.commands.workflows.import_workflow_from_local_path import cli as import_workflow_from_local_path
from parsec.commands.workflows.invoke_workflow import cli as invoke_workflow
from parsec.commands.workflows.run_invocation_step_action import cli as run_invocation_step_action
from parsec.commands.workflows.run_workflow import cli as run_workflow
from parsec.commands.workflows.show_invocation import cli as show_invocation
from parsec.commands.workflows.show_invocation_step import cli as show_invocation_step
from parsec.commands.workflows.show_workflow import cli as show_workflow


@click.group()
def cli():
    pass


cli.add_command(cancel_invocation)
cli.add_command(delete_workflow)
cli.add_command(export_workflow_dict)
cli.add_command(export_workflow_to_local_path)
cli.add_command(get_invocations)
cli.add_command(get_workflow_inputs)
cli.add_command(get_workflows)
cli.add_command(import_shared_workflow)
cli.add_command(import_workflow_dict)
cli.add_command(import_workflow_from_local_path)
cli.add_command(invoke_workflow)
cli.add_command(run_invocation_step_action)
cli.add_command(run_workflow)
cli.add_command(show_invocation)
cli.add_command(show_invocation_step)
cli.add_command(show_workflow)
