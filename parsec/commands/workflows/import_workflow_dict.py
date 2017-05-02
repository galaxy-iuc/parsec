import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('import_workflow_dict')
@click.argument("workflow_dict", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, workflow_dict):
    """Imports a new workflow given a dictionary representing a previously exported workflow.
    """
    return ctx.gi.workflows.import_workflow_dict(json_loads(workflow_dict))
