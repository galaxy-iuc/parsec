import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('update_workflow')
@click.argument("workflow_id", type=str)
@click.option(
    "--annotation",
    help="New annotation for the workflow",
    type=str
)
@click.option(
    "--menu_entry",
    help="Whether the workflow should appear in the user's menu",
    is_flag=True
)
@click.option(
    "--name",
    help="New name of the workflow",
    type=str
)
@click.option(
    "--tags",
    help="Replace workflow tags with the given list",
    type=str,
    multiple=True
)
@click.option(
    "--workflow",
    help="dictionary representing the workflow to be updated",
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, workflow_id, annotation=None, menu_entry=None, name=None, tags=None, workflow=None):
    """Update a given workflow.

Output:

    Dictionary representing the updated workflow
    """
    kwargs = {}
    if annotation and len(annotation) > 0:
        kwargs['annotation'] = annotation
    if menu_entry is not None:
        kwargs['menu_entry'] = menu_entry
    if name and len(name) > 0:
        kwargs['name'] = name

    return ctx.gi.workflows.update_workflow(workflow_id, **kwargs)
