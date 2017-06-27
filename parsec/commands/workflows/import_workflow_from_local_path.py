import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output, _arg_split

@click.command('import_workflow_from_local_path')
@click.argument("file_local_path", type=str)


@pass_context
@custom_exception
@dict_output
def cli(ctx, file_local_path):
    """Imports a new workflow given the path to a file containing a previously exported workflow.

Output:

    
    """
    return ctx.gi.workflows.import_workflow_from_local_path(file_local_path)
