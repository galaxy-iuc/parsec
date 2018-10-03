import click
from parsec.cli import pass_context
from parsec.decorators import custom_exception, dict_output


@click.command('export_workflow_json')
@click.argument("workflow_id")
@pass_context
@custom_exception
@dict_output
def cli(ctx, workflow_id):
    """.. deprecated:: 0.9.0 Use :meth:`export_workflow_dict` instead.

Output:

    
    """
    return ctx.gi.workflows.export_workflow_json(workflow_id)
