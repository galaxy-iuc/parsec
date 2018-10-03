import click
from parsec.cli import pass_context
from parsec.decorators import custom_exception, dict_output


@click.command('import_workflow_json')
@click.argument("workflow_json", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, workflow_json):
    """.. deprecated:: 0.9.0 Use :meth:`import_workflow_dict` instead.

Output:

    
    """
    return ctx.gi.workflows.import_workflow_json(json_loads(workflow_json))
