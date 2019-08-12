import click
from parsec.commands.toolshed_tools.search_tools import cli as search_tools


@click.group()
def cli():
    pass


cli.add_command(search_tools)
