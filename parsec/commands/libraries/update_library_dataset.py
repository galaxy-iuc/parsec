import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, dict_output


@click.command('update_library_dataset')
@click.argument("dataset_id", type=str)
@click.option(
    "--file_ext",
    help="Replace library dataset extension (must exist in the Galaxy registry)",
    type=str
)
@click.option(
    "--genome_build",
    help="Replace library dataset genome build (dbkey)",
    type=str
)
@click.option(
    "--misc_info",
    help="Replace library dataset misc_info with given string",
    type=str
)
@click.option(
    "--name",
    help="Replace library dataset name with the given string",
    type=str
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, dataset_id, file_ext=None, genome_build=None, misc_info=None, name=None):
    """Update library dataset metadata. Some of the attributes that can be modified are documented below.

Output:

    details of the updated dataset
    """
    kwargs = {}
    if file_ext and len(file_ext) > 0:
        kwargs['file_ext'] = file_ext
    if genome_build and len(genome_build) > 0:
        kwargs['genome_build'] = genome_build
    if misc_info and len(misc_info) > 0:
        kwargs['misc_info'] = misc_info
    if name and len(name) > 0:
        kwargs['name'] = name

    return ctx.gi.libraries.update_library_dataset(dataset_id, **kwargs)
