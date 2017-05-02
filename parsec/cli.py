from __future__ import absolute_import
import os
import sys
import click

from .io import error
from .config import read_global_config  # noqa, ditto
from .galaxy import get_galaxy_instance, get_toolshed_instance
from parsec import __version__  # noqa, ditto


CONTEXT_SETTINGS = dict(auto_envvar_prefix='PARSEC')

class Context(object):

    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()
        self._global_config = None

    @property
    def global_config(self):
        if self._global_config is None:
            self._global_config = read_global_config()
        return self._global_config

    def log(self, msg, *args):
        """Logs a message to stderr."""
        if args:
            msg %= args
        click.echo(msg, file=sys.stderr)

    def vlog(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log(msg, *args)


pass_context = click.make_pass_decorator(Context, ensure=True)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                          'commands'))


def list_cmds():
    rv = []
    for filename in os.listdir(cmd_folder):
        if filename.endswith('.py') and \
           filename.startswith('cmd_'):
            rv.append(filename[len("cmd_"):-len(".py")])
    rv.sort()
    return rv

def name_to_command(name):
    try:
        if sys.version_info[0] == 2:
            name = name.encode('ascii', 'replace')
        mod_name = 'parsec.commands.cmd_' + name
        mod = __import__(mod_name, None, None, ['cli'])
    except ImportError as e:
        error("Problem loading command %s, exception %s" % (name, e))
        return
    return mod.cli


class ParsecCLI(click.MultiCommand):

    def list_commands(self, ctx):
        return list_cmds()

    def get_command(self, ctx, name):
        return name_to_command(name)


@click.command(cls=ParsecCLI, context_settings=CONTEXT_SETTINGS)
@click.version_option(__version__)
@click.option('-v', '--verbose', is_flag=True,
              help='Enables verbose mode.')
@click.option(
    "--galaxy_instance",
    help='name of galaxy instance from ~/.planemo.yml',
    default='__default',
    required=True
)
@pass_context
def parsec(ctx, galaxy_instance, verbose):
    """Command line wrappers around BioBlend functions. While this sounds unexciting, with parsec and jq you can easily build powerful command line scripts."""
    # We abuse this, knowing that calls to one will fail.
    try:
        ctx.gi = get_galaxy_instance(galaxy_instance)
        ctx.ti = get_toolshed_instance(galaxy_instance)
    except TypeError:
        ctx.log("Could not access Toolshed/Galaxy instance configuration")
    ctx.verbose = verbose
