import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('show_data_table')
@click.argument("data_table_id", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, data_table_id):
    """Get details of a given data table.

Output:

    A description of the given data table and its content.
          For example::

            {"columns": ["value", "dbkey", "name", "path"],
             "fields": [["test id",
               "test",
               "test name",
               "/opt/galaxy-dist/tool-data/test/seq/test id.fa"]],
             "model_class": "TabularToolDataTable",
             "name": "all_fasta"}
    """
    return ctx.gi.tool_data.show_data_table(data_table_id)
