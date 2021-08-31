import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('requirements')
@click.argument("tool_id", type=str)
@pass_context
@custom_exception
@json_output
def cli(ctx, tool_id):
    """Return the resolver status for a specific tool. This functionality is available only to Galaxy admins.

Output:

    List containing a resolver status dict for each tool
          requirement. For example::

            [{'cacheable': False,
              'dependency_resolver': {'auto_init': True,
                                      'auto_install': False,
                                      'can_uninstall_dependencies': True,
                                      'ensure_channels': 'iuc,conda-forge,bioconda,defaults',
                                      'model_class': 'CondaDependencyResolver',
                                      'prefix': '/mnt/galaxy/tool_dependencies/_conda',
                                      'resolver_type': 'conda',
                                      'resolves_simple_dependencies': True,
                                      'use_local': False,
                                      'versionless': False},
              'dependency_type': 'conda',
              'environment_path': '/mnt/galaxy/tool_dependencies/_conda/envs/__blast@2.10.1',
              'exact': True,
              'model_class': 'MergedCondaDependency',
              'name': 'blast',
              'version': '2.10.1'}]
    """
    return ctx.gi.tools.requirements(tool_id)
