import click
from parsec.commands.tool_dependencies.summarize_toolbox import cli as summarize_toolbox


@click.group()
def cli():
    pass


cli.add_command(summarize_toolbox)
