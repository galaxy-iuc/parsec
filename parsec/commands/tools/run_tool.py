import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('run_tool')
@click.argument("history_id", type=str)
@click.argument("tool_id", type=str)
@click.argument("tool_inputs", type=str)
@pass_context
@custom_exception
@dict_output
def cli(ctx, history_id, tool_id, tool_inputs):
    """Runs tool specified by ``tool_id`` in history indicated by ``history_id`` with inputs from ``dict`` ``tool_inputs``.

Output:

    Information about outputs and job
          For example::

            {
              "outputs": [
                {
                  "misc_blurb": "queued",
                  "peek": null,
                  "update_time": "2019-05-08T12:26:16.069798",
                  "data_type": "galaxy.datatypes.tabular.Tabular",
                  "tags": [],
                  "deleted": false,
                  "history_id": "df8fe5ddadbf3ab1",
                  "metadata_column_names": null,
                  "metadata_delimiter": "	",
                  "visible": true,
                  "genome_build": "?",
                  "create_time": "2019-05-08T12:26:15.997739",
                  "hid": 42,
                  "file_size": 0,
                  "metadata_data_lines": null,
                  "file_ext": "tabular",
                  "id": "aeb65580396167f3",
                  "misc_info": null,
                  "hda_ldda": "hda",
                  "history_content_type": "dataset",
                  "name": "Cut on data 1",
                  "metadata_columns": null,
                  "uuid": "d91d10af-7546-45be-baa9-902010661466",
                  "state": "new",
                  "metadata_comment_lines": null,
                  "model_class": "HistoryDatasetAssociation",
                  "metadata_dbkey": "?",
                  "output_name": "out_file1",
                  "purged": false,
                  "metadata_column_types": null
                }
              ],
              "implicit_collections": [],
              "jobs": [
                {
                  "tool_id": "cut1",
                  "update_time": "2019-05-08T12:26:16.067389",
                  "exit_code": null,
                  "state": "new",
                  "create_time": "2019-05-08T12:26:16.067372",
                  "model_class": "Job",
                  "id": "7dd125b61b35d782"
                }
              ],
              "output_collections": []
            }

        The ``tool_inputs`` dict should contain input datasets and parameters
        in the (largely undocumented) format used by the Galaxy API.
        Some examples can be found in `Galaxy's API test suite
        <https://github.com/galaxyproject/galaxy/blob/dev/test/api/test_tools.py>`_.
    """
    return ctx.gi.tools.run_tool(history_id, tool_id, json_loads(tool_inputs))
