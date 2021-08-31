import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('run_tool')
@click.argument("history_id", type=str)
@click.argument("tool_id", type=str)
@click.argument("tool_inputs", type=str)
@click.option(
    "--input_format",
    help="input format for the payload. Possible values are the default 'legacy' (where inputs nested inside conditionals or repeats are identified with e.g. '<conditional_name>|<input_name>') or '21.01' (where inputs inside conditionals or repeats are nested elements).",
    default="legacy",
    show_default=True,
    type=str
)
@pass_context
@custom_exception
@json_output
def cli(ctx, history_id, tool_id, tool_inputs, input_format="legacy"):
    """Runs tool specified by ``tool_id`` in history indicated by ``history_id`` with inputs from ``dict`` ``tool_inputs``.

Output:

    Information about outputs and job
          For example::

            {'implicit_collections': [],
             'jobs': [{'create_time': '2019-05-08T12:26:16.067372',
                       'exit_code': None,
                       'id': '7dd125b61b35d782',
                       'model_class': 'Job',
                       'state': 'new',
                       'tool_id': 'cut1',
                       'update_time': '2019-05-08T12:26:16.067389'}],
             'output_collections': [],
             'outputs': [{'create_time': '2019-05-08T12:26:15.997739',
                          'data_type': 'galaxy.datatypes.tabular.Tabular',
                          'deleted': False,
                          'file_ext': 'tabular',
                          'file_size': 0,
                          'genome_build': '?',
                          'hda_ldda': 'hda',
                          'hid': 42,
                          'history_content_type': 'dataset',
                          'history_id': 'df8fe5ddadbf3ab1',
                          'id': 'aeb65580396167f3',
                          'metadata_column_names': None,
                          'metadata_column_types': None,
                          'metadata_columns': None,
                          'metadata_comment_lines': None,
                          'metadata_data_lines': None,
                          'metadata_dbkey': '?',
                          'metadata_delimiter': '	',
                          'misc_blurb': 'queued',
                          'misc_info': None,
                          'model_class': 'HistoryDatasetAssociation',
                          'name': 'Cut on data 1',
                          'output_name': 'out_file1',
                          'peek': None,
                          'purged': False,
                          'state': 'new',
                          'tags': [],
                          'update_time': '2019-05-08T12:26:16.069798',
                          'uuid': 'd91d10af-7546-45be-baa9-902010661466',
                          'visible': True}]}

        The ``tool_inputs`` dict should contain input datasets and parameters
        in the (largely undocumented) format used by the Galaxy API.
        Some examples can be found in `Galaxy's API test suite
        <https://github.com/galaxyproject/galaxy/blob/dev/lib/galaxy_test/api/test_tools.py>`_.
    """
    return ctx.gi.tools.run_tool(history_id, tool_id, tool_inputs, input_format=input_format)
