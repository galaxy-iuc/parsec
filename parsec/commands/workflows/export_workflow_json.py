import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('export_workflow_json')
@click.argument("workflow_id")


@pass_context
@bioblend_exception
@dict_output
def cli(ctx, workflow_id):
    """.. deprecated:: 0.9.0 Use :meth:`export_workflow_dict` instead.
    """
    return ctx.gi.workflows.export_workflow_json(workflow_id)
