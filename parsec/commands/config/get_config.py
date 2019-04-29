import click
from parsec.cli import pass_context, json_loads
from parsec.decorators import custom_exception, list_output


@click.command('get_config')
@pass_context
@custom_exception
@list_output
def cli(ctx):
    """Get a list of attributes about the Galaxy instance. More attributes will be present if the user is an admin.

Output:

    A list of attributes.
          For example::

            {u'allow_library_path_paste': False,
             u'allow_user_creation': True,
             u'allow_user_dataset_purge': True,
             u'allow_user_deletion': False,
             u'enable_unique_workflow_defaults': False,
             u'ftp_upload_dir': u'/SOMEWHERE/galaxy/ftp_dir',
             u'ftp_upload_site': u'galaxy.com',
             u'library_import_dir': u'None',
             u'logo_url': None,
             u'support_url': u'https://galaxyproject.org/support',
             u'terms_url': None,
             u'user_library_import_dir': None,
             u'wiki_url': u'https://galaxyproject.org/'}
    """
    return ctx.gi.config.get_config()
