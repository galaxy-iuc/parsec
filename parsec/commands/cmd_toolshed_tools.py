import click
from parsec.commands.toolshed_tools.search_tools import cli as func0


@click.group()
def cli():
    pass


cli.add_command(func0)
