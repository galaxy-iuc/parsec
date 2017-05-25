import click
from parsec.commands.tools.get_tool_panel import cli as func0
from parsec.commands.tools.get_tools import cli as func1
from parsec.commands.tools.install_dependencies import cli as func2
from parsec.commands.tools.paste_content import cli as func3
from parsec.commands.tools.put_url import cli as func4
from parsec.commands.tools.run_tool import cli as func5
from parsec.commands.tools.show_tool import cli as func6
from parsec.commands.tools.upload_file import cli as func7
from parsec.commands.tools.upload_from_ftp import cli as func8

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
