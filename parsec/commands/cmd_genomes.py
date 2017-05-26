import click
from parsec.commands.genomes.get_genomes import cli as func0
from parsec.commands.genomes.install_genome import cli as func1
from parsec.commands.genomes.show_genome import cli as func2

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
