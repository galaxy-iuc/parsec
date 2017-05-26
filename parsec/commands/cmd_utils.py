import click
from parsec.commands.utils.wait_on_invocation import cli as func0
from parsec.commands.utils.xunit_xargs import cli as func1
from parsec.commands.utils.cmp import cli as func2

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
