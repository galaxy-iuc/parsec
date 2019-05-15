import click
from parsec.commands.datatypes.get_datatypes import cli as get_datatypes
from parsec.commands.datatypes.get_sniffers import cli as get_sniffers


@click.group()
def cli():
    pass


cli.add_command(get_datatypes)
cli.add_command(get_sniffers)
