import click
from parsec.commands.forms.create_form import cli as create_form
from parsec.commands.forms.get_forms import cli as get_forms
from parsec.commands.forms.show_form import cli as show_form


@click.group()
def cli():
    pass


cli.add_command(create_form)
cli.add_command(get_forms)
cli.add_command(show_form)
