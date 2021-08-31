import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_invocation_biocompute_object')
@click.argument("invocation_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, invocation_id):
    """Get a BioCompute object for an invocation.

Output:

    The BioCompute object
    """
    return ctx.gi.invocations.get_invocation_biocompute_object(invocation_id)
