import click
from parsec.commands.tools.get_tool_panel import cli as get_tool_panel
from parsec.commands.tools.get_tools import cli as get_tools
from parsec.commands.tools.install_dependencies import cli as install_dependencies
from parsec.commands.tools.paste_content import cli as paste_content
from parsec.commands.tools.put_url import cli as put_url
from parsec.commands.tools.run_tool import cli as run_tool
from parsec.commands.tools.show_tool import cli as show_tool
from parsec.commands.tools.upload_file import cli as upload_file
from parsec.commands.tools.upload_from_ftp import cli as upload_from_ftp


@click.group()
def cli():
    pass


cli.add_command(get_tool_panel)
cli.add_command(get_tools)
cli.add_command(install_dependencies)
cli.add_command(paste_content)
cli.add_command(put_url)
cli.add_command(run_tool)
cli.add_command(show_tool)
cli.add_command(upload_file)
cli.add_command(upload_from_ftp)
