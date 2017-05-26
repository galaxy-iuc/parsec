import click
from parsec.commands.jobs.get_jobs import cli as func0
from parsec.commands.jobs.get_state import cli as func1
from parsec.commands.jobs.search_jobs import cli as func2
from parsec.commands.jobs.show_job import cli as func3

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
cli.add_command(func3)
