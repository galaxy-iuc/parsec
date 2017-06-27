import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output, _arg_split

@click.command('delete_folder')
@click.argument("folder_id", type=str)

@click.option(
    "--undelete",
    help="If set to True, the folder will be undeleted (i.e. the `deleted` mark will be removed)",
    is_flag=True
)

@pass_context
@custom_exception
@dict_output
def cli(ctx, folder_id, undelete=False):
    """Marks the folder with the given ``id`` as `deleted` (or removes the `deleted` mark if the `undelete` param is True).

Output:

    
    """
    return ctx.gi.folders.delete_folder(folder_id, undelete=undelete)
