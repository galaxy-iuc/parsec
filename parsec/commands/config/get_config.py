import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, json_output


@click.command('get_config')
@pass_context
@custom_exception
@json_output
def cli(ctx):
    """Get a list of attributes about the Galaxy instance. More attributes will be present if the user is an admin.

Output:

    A list of attributes.
          For example::

            {'allow_library_path_paste': False,
             'allow_user_creation': True,
             'allow_user_dataset_purge': True,
             'allow_user_deletion': False,
             'enable_unique_workflow_defaults': False,
             'ftp_upload_dir': '/SOMEWHERE/galaxy/ftp_dir',
             'ftp_upload_site': 'galaxy.com',
             'library_import_dir': 'None',
             'logo_url': None,
             'support_url': 'https://galaxyproject.org/support',
             'terms_url': None,
             'user_library_import_dir': None,
             'wiki_url': 'https://galaxyproject.org/'}
    """
    return ctx.gi.config.get_config()
