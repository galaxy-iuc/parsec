import click
from parsec.commands.libraries.copy_from_dataset import cli as copy_from_dataset
from parsec.commands.libraries.create_folder import cli as create_folder
from parsec.commands.libraries.create_library import cli as create_library
from parsec.commands.libraries.delete_library import cli as delete_library
from parsec.commands.libraries.delete_library_dataset import cli as delete_library_dataset
from parsec.commands.libraries.get_folders import cli as get_folders
from parsec.commands.libraries.get_libraries import cli as get_libraries
from parsec.commands.libraries.get_library_permissions import cli as get_library_permissions
from parsec.commands.libraries.set_library_permissions import cli as set_library_permissions
from parsec.commands.libraries.show_dataset import cli as show_dataset
from parsec.commands.libraries.show_folder import cli as show_folder
from parsec.commands.libraries.show_library import cli as show_library
from parsec.commands.libraries.update_library_dataset import cli as update_library_dataset
from parsec.commands.libraries.upload_file_contents import cli as upload_file_contents
from parsec.commands.libraries.upload_file_from_local_path import cli as upload_file_from_local_path
from parsec.commands.libraries.upload_file_from_server import cli as upload_file_from_server
from parsec.commands.libraries.upload_file_from_url import cli as upload_file_from_url
from parsec.commands.libraries.upload_from_galaxy_filesystem import cli as upload_from_galaxy_filesystem
from parsec.commands.libraries.wait_for_dataset import cli as wait_for_dataset


@click.group()
def cli():
    pass


cli.add_command(copy_from_dataset)
cli.add_command(create_folder)
cli.add_command(create_library)
cli.add_command(delete_library)
cli.add_command(delete_library_dataset)
cli.add_command(get_folders)
cli.add_command(get_libraries)
cli.add_command(get_library_permissions)
cli.add_command(set_library_permissions)
cli.add_command(show_dataset)
cli.add_command(show_folder)
cli.add_command(show_library)
cli.add_command(update_library_dataset)
cli.add_command(upload_file_contents)
cli.add_command(upload_file_from_local_path)
cli.add_command(upload_file_from_server)
cli.add_command(upload_file_from_url)
cli.add_command(upload_from_galaxy_filesystem)
cli.add_command(wait_for_dataset)
