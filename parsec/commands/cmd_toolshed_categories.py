import click
from parsec.commands.toolshed_categories.get_categories import cli as func0
from parsec.commands.toolshed_categories.show_category import cli as func1

@click.group()
def cli():
    pass

cli.add_command(func0)
cli.add_command(func1)
