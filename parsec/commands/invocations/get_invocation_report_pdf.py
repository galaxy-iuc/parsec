import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('get_invocation_report_pdf')
@click.argument("invocation_id", type=str)
@click.argument("file_path", type=str)
@click.option(
    "--chunk_size",
    help="",
    default="4096",
    show_default=True
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, invocation_id, file_path, chunk_size=4096):
    """Get a PDF report for an invocation.

Output:


    """
    return ctx.gi.invocations.get_invocation_report_pdf(invocation_id, file_path, chunk_size=chunk_size)
