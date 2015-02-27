import click

from parsec.cli import pass_context
from parsec.io import error
from parsec import options
from parsec.galaxy import get_galaxy_instance


@click.command('new_api_key')
@options.galaxy_instance()

@click.option(
    '--id',
    help="Encoded ID of user",
)

@pass_context
def cli(ctx, galaxy_instance, id):
    """(Re)generate API key for user
    """
    global_config = ctx.global_config

    if 'admin' not in global_config[galaxy_instance] or not \
            global_config[galaxy_instance]['admin']:
        error("This must be an admin API key (set admin: True in ~/.planemo.yml)")
        return -2

    gi = get_galaxy_instance(galaxy_instance)

    print gi.users.create_user_apikey(id)
