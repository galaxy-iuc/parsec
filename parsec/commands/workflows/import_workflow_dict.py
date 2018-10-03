import click
from parsec.cli import pass_context
from parsec.decorators import custom_exception, dict_output


@click.command('import_workflow_dict')
@click.argument("workflow_dict", type=str)
@click.option(
    "--publish",
    help="if ``True`` the uploaded workflow will be published; otherwise it will be visible only by the user which uploads it (default)",
    is_flag=True
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, workflow_dict, publish=False):
    """Imports a new workflow given a dictionary representing a previously exported workflow.

Output:

    
    """
    return ctx.gi.workflows.import_workflow_dict(json_loads(workflow_dict), publish=publish)
