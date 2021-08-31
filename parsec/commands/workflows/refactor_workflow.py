import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('refactor_workflow')
@click.argument("workflow_id", type=str)
@click.option("--actions", type=str, multiple=True, required=True)
@click.option(
    "--dry_run",
    help="When true, perform a dry run where the existing workflow is preserved. The refactored workflow is returned in the output of the method, but not saved on the Galaxy server.",
    is_flag=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, workflow_id, actions, dry_run=False):
    """Refactor workflow with given actions.

Output:

    Dictionary containing logged messages for the executed actions
                 and the refactored workflow.
    """
    return ctx.gi.workflows.refactor_workflow(workflow_id, actions, dry_run=dry_run)
