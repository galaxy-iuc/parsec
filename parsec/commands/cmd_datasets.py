import click
from parsec.commands.datasets.download_dataset import cli as download_dataset
from parsec.commands.datasets.get_datasets import cli as get_datasets
from parsec.commands.datasets.publish_dataset import cli as publish_dataset
from parsec.commands.datasets.show_dataset import cli as show_dataset
from parsec.commands.datasets.update_permissions import cli as update_permissions
from parsec.commands.datasets.wait_for_dataset import cli as wait_for_dataset


@click.group()
def cli():
    pass


cli.add_command(download_dataset)
cli.add_command(get_datasets)
cli.add_command(publish_dataset)
cli.add_command(show_dataset)
cli.add_command(update_permissions)
cli.add_command(wait_for_dataset)
