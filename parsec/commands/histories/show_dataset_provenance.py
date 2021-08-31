import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('show_dataset_provenance')
@click.argument("history_id", type=str)
@click.argument("dataset_id", type=str)
@click.option(
    "--follow",
    help="If ``True``, recursively fetch dataset provenance information for all inputs and their inputs, etc.",
    is_flag=True
)
@pass_context
@custom_exception
@json_output
def cli(ctx, history_id, dataset_id, follow=False):
    """Get details related to how dataset was created (``id``, ``job_id``, ``tool_id``, ``stdout``, ``stderr``, ``parameters``, ``inputs``, etc...).

Output:

    Dataset provenance information
          For example::

            {'id': '6fbd9b2274c62ebe',
             'job_id': '5471ba76f274f929',
             'parameters': {'chromInfo': '"/usr/local/galaxy/galaxy-dist/tool-data/shared/ucsc/chrom/mm9.len"',
                            'dbkey': '"mm9"',
                            'experiment_name': '"H3K4me3_TAC_MACS2"',
                            'input_chipseq_file1': {'id': '6f0a311a444290f2',
                                                    'uuid': 'null'},
                            'input_control_file1': {'id': 'c21816a91f5dc24e',
                                                    'uuid': '16f8ee5e-228f-41e2-921e-a07866edce06'},
                            'major_command': '{"gsize": "2716965481.0", "bdg": "False", "__current_case__": 0, "advanced_options": {"advanced_options_selector": "off", "__current_case__": 1}, "input_chipseq_file1": 104715, "xls_to_interval": "False", "major_command_selector": "callpeak", "input_control_file1": 104721, "pq_options": {"pq_options_selector": "qvalue", "qvalue": "0.05", "__current_case__": 1}, "bw": "300", "nomodel_type": {"nomodel_type_selector": "create_model", "__current_case__": 1}}'},
             'stderr': '',
             'stdout': '',
             'tool_id': 'toolshed.g2.bx.psu.edu/repos/ziru-zhou/macs2/modencode_peakcalling_macs2/2.0.10.2',
             'uuid': '5c0c43f5-8d93-44bd-939d-305e82f213c6'}
    """
    return ctx.gi.histories.show_dataset_provenance(history_id, dataset_id, follow=follow)
