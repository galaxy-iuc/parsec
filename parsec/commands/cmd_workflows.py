import click
from parsec.commands.workflows.cancel_invocation import cli as func0
from parsec.commands.workflows.delete_workflow import cli as func1
from parsec.commands.workflows.export_workflow_dict import cli as func2
from parsec.commands.workflows.export_workflow_json import cli as func3
from parsec.commands.workflows.export_workflow_to_local_path import cli as func4
from parsec.commands.workflows.get_invocations import cli as func5
from parsec.commands.workflows.get_workflow_inputs import cli as func6
from parsec.commands.workflows.get_workflows import cli as func7
from parsec.commands.workflows.import_shared_workflow import cli as func8
from parsec.commands.workflows.import_workflow_dict import cli as func9
from parsec.commands.workflows.import_workflow_from_local_path import cli as func10
from parsec.commands.workflows.import_workflow_json import cli as func11
from parsec.commands.workflows.invoke_workflow import cli as func12
from parsec.commands.workflows.run_invocation_step_action import cli as func13
from parsec.commands.workflows.run_workflow import cli as func14
from parsec.commands.workflows.show_invocation import cli as func15
from parsec.commands.workflows.show_invocation_step import cli as func16
from parsec.commands.workflows.show_workflow import cli as func17

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
cli.add_command(func3)
cli.add_command(func4)
cli.add_command(func5)
cli.add_command(func6)
cli.add_command(func7)
cli.add_command(func8)
cli.add_command(func9)
cli.add_command(func10)
cli.add_command(func11)
cli.add_command(func12)
cli.add_command(func13)
cli.add_command(func14)
cli.add_command(func15)
cli.add_command(func16)
cli.add_command(func17)
