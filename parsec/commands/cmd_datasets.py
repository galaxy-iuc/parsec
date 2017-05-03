import click
from parsec.commands.datasets.download_dataset import cli as func0
from parsec.commands.datasets.show_dataset import cli as func1

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
