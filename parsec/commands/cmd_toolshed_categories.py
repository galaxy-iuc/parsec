import click
from parsec.commands.toolshed_categories.get_categories import cli as get_categories
from parsec.commands.toolshed_categories.show_category import cli as show_category


@click.group()
def cli():
    pass


cli.add_command(get_categories)
cli.add_command(show_category)
