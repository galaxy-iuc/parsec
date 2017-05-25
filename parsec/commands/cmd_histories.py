import click
from parsec.commands.histories.create_dataset_collection import cli as func0
from parsec.commands.histories.create_history import cli as func1
from parsec.commands.histories.create_history_tag import cli as func2
from parsec.commands.histories.delete_dataset import cli as func3
from parsec.commands.histories.delete_dataset_collection import cli as func4
from parsec.commands.histories.delete_history import cli as func5
from parsec.commands.histories.download_dataset import cli as func6
from parsec.commands.histories.download_history import cli as func7
from parsec.commands.histories.export_history import cli as func8
from parsec.commands.histories.get_current_history import cli as func9
from parsec.commands.histories.get_histories import cli as func10
from parsec.commands.histories.get_most_recently_used_history import cli as func11
from parsec.commands.histories.get_status import cli as func12
from parsec.commands.histories.show_dataset import cli as func13
from parsec.commands.histories.show_dataset_collection import cli as func14
from parsec.commands.histories.show_dataset_provenance import cli as func15
from parsec.commands.histories.show_history import cli as func16
from parsec.commands.histories.show_matching_datasets import cli as func17
from parsec.commands.histories.undelete_history import cli as func18
from parsec.commands.histories.update_dataset import cli as func19
from parsec.commands.histories.update_dataset_collection import cli as func20
from parsec.commands.histories.update_history import cli as func21
from parsec.commands.histories.upload_dataset_from_library import cli as func22

@click.group()
def cli():
	pass

cli.add_command(func0)
cli.add_command(func1)
cli.add_command(func2)
cli.add_command(func3)
cli.add_command(func4)
cli.add_command(func5)
cli.add_command(func6)
cli.add_command(func7)
cli.add_command(func8)
cli.add_command(func9)
cli.add_command(func10)
cli.add_command(func11)
cli.add_command(func12)
cli.add_command(func13)
cli.add_command(func14)
cli.add_command(func15)
cli.add_command(func16)
cli.add_command(func17)
cli.add_command(func18)
cli.add_command(func19)
cli.add_command(func20)
cli.add_command(func21)
cli.add_command(func22)
