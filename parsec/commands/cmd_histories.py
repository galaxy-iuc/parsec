import click
from parsec.commands.histories.create_dataset_collection import cli as create_dataset_collection
from parsec.commands.histories.create_history import cli as create_history
from parsec.commands.histories.create_history_tag import cli as create_history_tag
from parsec.commands.histories.delete_dataset import cli as delete_dataset
from parsec.commands.histories.delete_dataset_collection import cli as delete_dataset_collection
from parsec.commands.histories.delete_history import cli as delete_history
from parsec.commands.histories.download_history import cli as download_history
from parsec.commands.histories.export_history import cli as export_history
from parsec.commands.histories.get_histories import cli as get_histories
from parsec.commands.histories.get_most_recently_used_history import cli as get_most_recently_used_history
from parsec.commands.histories.get_status import cli as get_status
from parsec.commands.histories.show_dataset import cli as show_dataset
from parsec.commands.histories.show_dataset_collection import cli as show_dataset_collection
from parsec.commands.histories.show_dataset_provenance import cli as show_dataset_provenance
from parsec.commands.histories.show_history import cli as show_history
from parsec.commands.histories.show_matching_datasets import cli as show_matching_datasets
from parsec.commands.histories.undelete_history import cli as undelete_history
from parsec.commands.histories.update_dataset import cli as update_dataset
from parsec.commands.histories.update_dataset_collection import cli as update_dataset_collection
from parsec.commands.histories.update_history import cli as update_history
from parsec.commands.histories.upload_dataset_from_library import cli as upload_dataset_from_library


@click.group()
def cli():
    pass


cli.add_command(create_dataset_collection)
cli.add_command(create_history)
cli.add_command(create_history_tag)
cli.add_command(delete_dataset)
cli.add_command(delete_dataset_collection)
cli.add_command(delete_history)
cli.add_command(download_history)
cli.add_command(export_history)
cli.add_command(get_histories)
cli.add_command(get_most_recently_used_history)
cli.add_command(get_status)
cli.add_command(show_dataset)
cli.add_command(show_dataset_collection)
cli.add_command(show_dataset_provenance)
cli.add_command(show_history)
cli.add_command(show_matching_datasets)
cli.add_command(undelete_history)
cli.add_command(update_dataset)
cli.add_command(update_dataset_collection)
cli.add_command(update_history)
cli.add_command(upload_dataset_from_library)
