import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_invocations')
@click.option(
    "--workflow_id",
    help="Encoded workflow ID to filter on",
    type=str
)
@click.option(
    "--history_id",
    help="Encoded history ID to filter on",
    type=str
)
@click.option(
    "--user_id",
    help="Encoded user ID to filter on. This must be your own user ID if your are not an admin user.",
    type=str
)
@click.option(
    "--include_terminal",
    help="Whether to include terminal states.",
    default="True",
    show_default=True,
    is_flag=True
)
@click.option(
    "--limit",
    help="Maximum number of invocations to return - if specified, the most recent invocations will be returned.",
    type=int
)
@click.option(
    "--view",
    help="Level of detail to return per invocation, either 'element' or 'collection'.",
    default="collection",
    show_default=True,
    type=str
)
@click.option(
    "--step_details",
    help="If 'view' is 'element', also include details on individual steps.",
    is_flag=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, workflow_id="", history_id="", user_id="", include_terminal=True, limit="", view="collection", step_details=False):
    """Get all workflow invocations, or select a subset by specifying optional arguments for filtering (e.g. a workflow ID).

Output:

    A list of workflow invocations.
          For example::

            [{'history_id': '2f94e8ae9edff68a',
              'id': 'df7a1f0c02a5b08e',
              'model_class': 'WorkflowInvocation',
              'state': 'new',
              'update_time': '2015-10-31T22:00:22',
              'uuid': 'c8aa2b1c-801a-11e5-a9e5-8ca98228593c',
              'workflow_id': '03501d7626bd192f'}]
    """
    return ctx.gi.invocations.get_invocations(workflow_id=workflow_id, history_id=history_id, user_id=user_id, include_terminal=include_terminal, limit=limit, view=view, step_details=step_details)
