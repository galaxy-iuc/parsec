import click
from parsec.commands.ftpfiles.get_ftp_files import cli as get_ftp_files
from parsec.commands.ftpfiles.module import cli as module


@click.group()
def cli():
    pass


cli.add_command(get_ftp_files)
cli.add_command(module)
