import click
from parsec.commands.forms.create_form import cli as func0
from parsec.commands.forms.get_forms import cli as func1
from parsec.commands.forms.show_form import cli as func2

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
