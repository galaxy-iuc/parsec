import click
from parsec.commands.visual.get_visualizations import cli as get_visualizations
from parsec.commands.visual.module import cli as module
from parsec.commands.visual.show_visualization import cli as show_visualization


@click.group()
def cli():
    pass


cli.add_command(get_visualizations)
cli.add_command(module)
cli.add_command(show_visualization)
