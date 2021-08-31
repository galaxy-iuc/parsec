import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_invocation_report_pdf')
@click.argument("invocation_id", type=str)
@click.argument("file_path", type=str)
@click.option(
    "--chunk_size",
    help="Size of chunks to requests, defaults to bioblend.CHUNK_SIZE",
    default="4096",
    show_default=True,
    type=int
)
@pass_context
@custom_exception
@json_output
def cli(ctx, invocation_id, file_path, chunk_size=4096):
    """Get a PDF report for an invocation.

Output:

    
    """
    return ctx.gi.invocations.get_invocation_report_pdf(invocation_id, file_path, chunk_size=chunk_size)
