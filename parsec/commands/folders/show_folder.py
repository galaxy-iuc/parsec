import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output, _arg_split

@click.command('show_folder')
@click.argument("folder_id", type=str)


@pass_context
@custom_exception
@dict_output
def cli(ctx, folder_id):
    """Display information about a folder.

Output:

     dictionary including details of the folder
        
    """
    return ctx.gi.folders.show_folder(folder_id)
