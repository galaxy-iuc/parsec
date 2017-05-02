import click
from parsec.commands.ftpfiles.get_ftp_files import cli as func0

@click.group()
def cli():
	pass

cli.add_command(func0)
