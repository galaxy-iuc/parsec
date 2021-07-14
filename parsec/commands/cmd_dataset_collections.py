import click
from parsec.commands.dataset_collections.download_dataset_collection import cli as download_dataset_collection
from parsec.commands.dataset_collections.show_dataset_collection import cli as show_dataset_collection
from parsec.commands.dataset_collections.wait_for_dataset_collection import cli as wait_for_dataset_collection


@click.group()
def cli():
    pass


cli.add_command(download_dataset_collection)
cli.add_command(show_dataset_collection)
cli.add_command(wait_for_dataset_collection)
