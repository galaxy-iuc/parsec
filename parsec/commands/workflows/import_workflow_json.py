import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output, _arg_split

@click.command('import_workflow_json')
@click.argument("workflow_json")


@pass_context
@custom_exception
@dict_output
def cli(ctx, workflow_json):
    """.. deprecated:: 0.9.0 Use :meth:`import_workflow_dict` instead.

Output:

    
    """
    return ctx.gi.workflows.import_workflow_json(workflow_json)
