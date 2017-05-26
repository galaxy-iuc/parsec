import click
from parsec.commands.libraries.copy_from_dataset import cli as func0
from parsec.commands.libraries.create_folder import cli as func1
from parsec.commands.libraries.create_library import cli as func2
from parsec.commands.libraries.delete_library import cli as func3
from parsec.commands.libraries.delete_library_dataset import cli as func4
from parsec.commands.libraries.get_folders import cli as func5
from parsec.commands.libraries.get_libraries import cli as func6
from parsec.commands.libraries.get_library_permissions import cli as func7
from parsec.commands.libraries.set_library_permissions import cli as func8
from parsec.commands.libraries.show_dataset import cli as func9
from parsec.commands.libraries.show_folder import cli as func10
from parsec.commands.libraries.show_library import cli as func11
from parsec.commands.libraries.upload_file_contents import cli as func12
from parsec.commands.libraries.upload_file_from_local_path import cli as func13
from parsec.commands.libraries.upload_file_from_server import cli as func14
from parsec.commands.libraries.upload_file_from_url import cli as func15
from parsec.commands.libraries.upload_from_galaxy_filesystem import cli as func16

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
