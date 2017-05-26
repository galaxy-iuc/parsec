import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import bioblend_exception, dict_output

@click.command('get_workflows')

@click.option(
    "--workflow_id",
    help="Encoded workflow ID (incompatible with ``name``)",
    type=str
)
@click.option(
    "--name",
    help="Filter by name of workflow (incompatible with ``workflow_id``). If multiple names match the given name, all the workflows matching the argument will be returned.",
    type=str
)
@click.option(
    "--published",
    help="if ``True``, return also published workflows",
    is_flag=True
)

@pass_context
@bioblend_exception
@dict_output
def cli(ctx, workflow_id="", name="", published=False):
    """Get all workflows or filter the specific one(s) via the provided ``name`` or ``workflow_id``. Provide only one argument, ``name`` or ``workflow_id``, but not both.
    """
    return ctx.gi.workflows.get_workflows(workflow_id=workflow_id, name=name, published=published)
