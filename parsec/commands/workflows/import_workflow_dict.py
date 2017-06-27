import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output, _arg_split

@click.command('import_workflow_dict')
@click.argument("workflow_dict", type=str)


@pass_context
@custom_exception
@dict_output
def cli(ctx, workflow_dict):
    """Imports a new workflow given a dictionary representing a previously exported workflow.

Output:

    
    """
    return ctx.gi.workflows.import_workflow_dict(json_loads(workflow_dict))
