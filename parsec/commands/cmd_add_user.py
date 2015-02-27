import click

from parsec.cli import pass_context
from parsec.io import error, info
from parsec import options
from parsec.galaxy import get_galaxy_instance
from parsec.decorators import bioblend_exception, dict_output


@click.command('add_user')
@options.galaxy_instance()

@click.option(
    '--username',
    help="Username for the new user",
    required=True,
)

@click.option(
    '--email',
    help="Email for the new user",
    required=True,
)

@click.option(
    '--password',
    help="Password for the new user",
    required=True,
)

@click.option(
    '--remote',
    is_flag=True,
    help="This galaxy instance is configured for REMOTE_USER",
)
@bioblend_exception
@dict_output
@pass_context
def cli(ctx, galaxy_instance, username, email, password, remote=False, **kwds):
    """Add a user to a galaxy instance
    """
    global_config = ctx.global_config

    if 'admin' not in global_config[galaxy_instance] or not \
            global_config[galaxy_instance]['admin']:
        error("This must be an admin API key (set admin: True in ~/.planemo.yml)")
        return -2

    gi = get_galaxy_instance(galaxy_instance)

    if remote:
        result = gi.users.create_remote_user(email)
    else:
        result = gi.users.create_local_user(username, email, password)

    info("Created user %(username)s with id %(id)s." % result)
    return result
