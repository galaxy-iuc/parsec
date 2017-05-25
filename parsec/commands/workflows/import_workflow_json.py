import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('import_workflow_json')
@click.argument("workflow_json", type=str)


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, workflow_json):
    """Imports a new workflow given a json representation of a previously exported workflow.
    """
    return ctx.gi.workflows.import_workflow_json(workflow_json)
