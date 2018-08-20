from __future__ import absolute_import
import os
import yaml
from xdg import XDG_CONFIG_HOME

DEFAULT_CONFIG = None

config_paths = []

# User can override by supplying env var
if 'PARSEC_GLOBAL_CONFIG_PATH' in os.environ:
    config_paths.append(os.environ['PARSEC_GLOBAL_CONFIG_PATH'])

# Fall back to xdg
if os.path.exists(XDG_CONFIG_HOME) and os.path.isdir(XDG_CONFIG_HOME):
    xdg_folder = os.path.join(XDG_CONFIG_HOME, 'galaxy-parsec')
    # This isn't great. But at least it only happens when XDG stuff is set?
    os.makedirs(xdg_folder)
    config_paths.append(os.path.join(xdg_folder, 'config.yml'))

# Fall back to home dir
config_paths.append('~/.parsec.yml')


def _get_path():
    for config_path in config_paths:
        # If we can find a file there, use it.
        path = os.path.expanduser(config_path)
        if os.path.exists(path):
            return path
   
    # Return the first thing even if it doesn't exist.
    return config_path[0]
      

def global_config_path():
    return _get_path() 


def set_global_config_path(path):
    config_paths = [path] + config_paths


def read_global_config():
    # Read the path if it exists, otherwise, return empty dict.
    config_path = _get_path()
    if not os.path.exists(config_path):
        return {}

    with open(config_path) as f:
        return yaml.load(f)
