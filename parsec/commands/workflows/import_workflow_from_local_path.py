import click
from parsec.cli import pass_context
from parsec.decorators import custom_exception, dict_output


@click.command('import_workflow_from_local_path')
@click.argument("file_local_path", type=str)
@click.option(
    "--publish",
    help="if ``True`` the uploaded workflow will be published; otherwise it will be visible only by the user which uploads it (default)",
    is_flag=True
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, file_local_path, publish=False):
    """Imports a new workflow given the path to a file containing a previously exported workflow.

Output:

    
    """
    return ctx.gi.workflows.import_workflow_from_local_path(file_local_path, publish=publish)
