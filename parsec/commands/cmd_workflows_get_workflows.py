import click

from parsec.cli import pass_context
from parsec.decorators import bioblend_exception, dict_output


@click.command('workflows_get_workflows')
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
    "--deleted",
    help="this parameter is deprecated and ignored, it will be removed in BioBlend 0.6",
    is_flag=True
)
@click.option(
    "--published",
    help="if ``True``, return also published workflows",
    is_flag=True
)
@pass_context
@bioblend_exception
@dict_output
def cli(ctx, workflow_id="", name="", deleted=False, published=False):
    """Get all workflows or filter the specific one(s) via the provided ``name`` or ``workflow_id``. Provide only one argument, ``name`` or ``workflow_id``, but not both.
    """
    return ctx.gi.workflows.get_workflows(
        workflow_id=workflow_id,
        name=name,
        deleted=deleted,
        published=published)
