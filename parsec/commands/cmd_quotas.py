import click
from parsec.commands.quotas.create_quota import cli as func0
from parsec.commands.quotas.delete_quota import cli as func1
from parsec.commands.quotas.get_quotas import cli as func2
from parsec.commands.quotas.show_quota import cli as func3
from parsec.commands.quotas.undelete_quota import cli as func4
from parsec.commands.quotas.update_quota import cli as func5

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
cli.add_command(func3)
cli.add_command(func4)
cli.add_command(func5)
