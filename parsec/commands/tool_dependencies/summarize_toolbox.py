import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('summarize_toolbox')
@click.option(
    "--index",
    help="index of the dependency resolver with respect to the dependency resolvers config file",
    type=int
)
@click.option(
    "--tool_ids",
    help="tool_ids to return when index_by=tools",
    type=str,
    multiple=True
)
@click.option(
    "--resolver_type",
    help="restrict to specified resolver type",
    type=str
)
@click.option(
    "--include_containers",
    help="include container resolvers in resolution",
    is_flag=True
)
@click.option(
    "--container_type",
    help="restrict to specified container type",
    type=str
)
@click.option(
    "--index_by",
    help="By default results are grouped by requirements. Set to 'tools' to return one entry per tool.",
    default="requirements",
    show_default=True,
    type=str
)
@pass_context
@custom_exception
@json_output
def cli(ctx, index="", tool_ids="", resolver_type="", include_containers=False, container_type="", index_by="requirements"):
    """Summarize requirements across toolbox (for Tool Management grid).

Output:

    dictified descriptions of the dependencies, with attribute
          `dependency_type: None` if no match was found.
          For example::

            [{'requirements': [{'name': 'galaxy_sequence_utils',
                                'specs': [],
                                'type': 'package',
                                'version': '1.1.4'},
                               {'name': 'bx-python',
                                'specs': [],
                                'type': 'package',
                                'version': '0.8.6'}],
              'status': [{'cacheable': False,
                          'dependency_type': None,
                          'exact': True,
                          'model_class': 'NullDependency',
                          'name': 'galaxy_sequence_utils',
                          'version': '1.1.4'},
                          {'cacheable': False,
                          'dependency_type': None,
                          'exact': True,
                          'model_class': 'NullDependency',
                          'name': 'bx-python',
                          'version': '0.8.6'}],
              'tool_ids': ['vcf_to_maf_customtrack1']}]

        .. note::
          This method can only be used with Galaxy ``release_20.01`` or later and requires
            the user to be an admin. It relies on an experimental API particularly tied to
            the GUI and therefore is subject to breaking changes.
    """
    return ctx.gi.tool_dependencies.summarize_toolbox(index=index, tool_ids=tool_ids, resolver_type=resolver_type, include_containers=include_containers, container_type=container_type, index_by=index_by)
