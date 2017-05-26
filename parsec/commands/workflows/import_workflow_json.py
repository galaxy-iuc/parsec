import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('import_workflow_json')
@click.argument("workflow_json")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, workflow_json):
    """.. deprecated:: 0.9.0 Use :meth:`import_workflow_dict` instead.
    """
    return ctx.gi.workflows.import_workflow_json(workflow_json)
