import click
from parsec.commands.datasets.download_dataset import cli as func0
from parsec.commands.datasets.show_stdout import cli as func1
from parsec.commands.datasets.show_stderr import cli as func2
from parsec.commands.datasets.show_dataset import cli as func3

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
cli.add_command(func3)
