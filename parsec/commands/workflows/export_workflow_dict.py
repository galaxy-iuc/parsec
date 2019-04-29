import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('export_workflow_dict')
@click.argument("workflow_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, workflow_id):
    """Exports a workflow.

Output:

    Dictionary representing the requested workflow
    """
    return ctx.gi.workflows.export_workflow_dict(workflow_id)
