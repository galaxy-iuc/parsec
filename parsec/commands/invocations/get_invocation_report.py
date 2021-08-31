import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_invocation_report')
@click.argument("invocation_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, invocation_id):
    """Get a Markdown report for an invocation.

Output:

    The invocation report.
          For example::

            {'markdown': '\n# Workflow Execution Summary of Example workflow\n\n
             ## Workflow Inputs\n\n\n## Workflow Outputs\n\n\n
             ## Workflow\n```galaxy\n
             workflow_display(workflow_id=f2db41e1fa331b3e)\n```\n',
             'render_format': 'markdown',
             'workflows': {'f2db41e1fa331b3e': {'name': 'Example workflow'}}}
    """
    return ctx.gi.invocations.get_invocation_report(invocation_id)
