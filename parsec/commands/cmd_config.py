import click
from parsec.commands.config.cmd_config_get_config import cli as ccgc


@click.group()
def cli():
    pass

cli.add_command(ccgc)
