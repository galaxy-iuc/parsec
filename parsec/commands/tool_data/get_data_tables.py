import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_data_tables')
@pass_context
@custom_exception
@list_output
def cli(ctx):
    """Get the list of all data tables.

Output:

    A list of dicts with details on individual data tables.
          For example::

            [{"model_class": "TabularToolDataTable", "name": "fasta_indexes"},
             {"model_class": "TabularToolDataTable", "name": "bwa_indexes"}]
    """
    return ctx.gi.tool_data.get_data_tables()
