import os

import click

from bioblend import galaxy
from parsec.cli import pass_context
from parsec import config
from parsec.io import warn, info

CONFIG_TEMPLATE = """## Parsec Global Configuration File.
# Each stanza should contian a single galaxy server to control.
#
# You can set the key __default to the name of a default instance
__default: local

local:
    key: "%(key)s"
    url: "%(url)s"
    # email: ""
    # password: ""
"""

SUCCESS_MESSAGE = (
    "Ready to go! Type `parsec` to get a list of commands you can execute."
)


@click.command("config_init")
@click.option(
    "--url",
    help="your Galaxy's URL",
    type=str
)
@click.option(
    "--api_key",
    help="your Galaxy API Key",
    type=str
)
@pass_context
def cli(ctx, url=None, api_key=None, admin=False, **kwds):
    """Help initialize global configuration (in home directory)
    """
    # TODO: prompt for values someday.
    click.echo("""
Welcome to
      ____   ____ _   _____   _____  ___   _____
     / __ \ / __ `/  / ___/  / ___/ / _ \ / ___/
    / /_/ // /_/ /  / /     (__  ) /  __// /__
   / .___/ \__,_/  /_/     /____/  \___/ \___/
  /_/ Galaxy at the Speed of Light
""")
    config_path = config.global_config_path()

    if os.path.exists(config_path):
        info("Your parsec configuration already exists. Please edit it instead: %s" % config_path)
        return 0

    while True:
        galaxy_url = url
        if url is None or len(url) == 0 :
            galaxy_url = click.prompt("Please entry your Galaxy's URL")
        galaxy_key = api_key
        if api_key is None or len(api_key) == 0 :
            galaxy_key = click.prompt("Please entry your Galaxy API Key")
        info("Testing connection...")
        try:
            gi = galaxy.GalaxyInstance(galaxy_url, galaxy_key)
            if 'version_major' in gi.config.get_config():
                # Ok, success
                info("Ok! Everything looks good.")
                break
            else:
                warn("Error, we could not access the configuration data for your instance.")
                should_break = click.prompt("Continue despite inability to contact this Galaxy Instance? [y/n]")
                if should_break in ('Y', 'y'):
                    break
        except Exception as e:
            warn("Error, we could not access the configuration data for your instance.")
            should_break = click.prompt("Continue despite inability to contact this Galaxy Instance? [y/n]")
            if should_break in ('Y', 'y'):
                break

    if os.path.exists(config_path):
        warn("File %s already exists, refusing to overwrite." % config_path)
        return -1
    with open(config_path, "w") as f:
        f.write(
            CONFIG_TEMPLATE % {
                'key': galaxy_key,
                'url': galaxy_url,
            })
        info(SUCCESS_MESSAGE)
