import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('import_workflow_from_local_path')
@click.argument("file_local_path", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, file_local_path):
    """Imports a new workflow given the path to a file containing a previously exported workflow.
    """
    return ctx.gi.workflows.import_workflow_from_local_path(file_local_path)
