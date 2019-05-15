import click
from parsec.commands.config.get_config import cli as get_config
from parsec.commands.config.get_version import cli as get_version


@click.group()
def cli():
    pass


cli.add_command(get_config)
cli.add_command(get_version)
