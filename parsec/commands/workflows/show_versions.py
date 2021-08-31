import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('show_versions')
@click.argument("workflow_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, workflow_id):
    """Get versions for a workflow.

Output:

    Ordered list of version descriptions for this workflow
    """
    return ctx.gi.workflows.show_versions(workflow_id)
