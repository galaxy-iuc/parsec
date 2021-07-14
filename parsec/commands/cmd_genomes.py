import click
from parsec.commands.genomes.get_genomes import cli as get_genomes
from parsec.commands.genomes.install_genome import cli as install_genome
from parsec.commands.genomes.show_genome import cli as show_genome


@click.group()
def cli():
    pass


cli.add_command(get_genomes)
cli.add_command(install_genome)
cli.add_command(show_genome)
