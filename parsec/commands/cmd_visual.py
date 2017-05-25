import click
from parsec.commands.visual.get_visualizations import cli as func0
from parsec.commands.visual.show_visualization import cli as func1

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
