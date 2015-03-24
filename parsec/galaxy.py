import os
from bioblend import galaxy, toolshed
from .config import read_global_config, global_config_path
from .io import warn

def get_instance(instance_name=None):
    # I don't like reading the config twice.
    conf = read_global_config()
    if not os.path.exists(global_config_path()):
        # Probably creating the file for the first time.
        warn("No parsec config file found, continuning anyway...")
        return None

    if instance_name is None or instance_name == '__default':
        try:
            instance_name = conf['__default']
        except KeyError:
            raise Exception("Unknown Galaxy instance and no __default provided")
    if instance_name not in conf:
        raise Exception("Unknown Galaxy instance; check spelling or add to ~/.planemo.yml")
    return conf

def get_galaxy_instance(instance_name=None):
    conf = get_instance(instance_name=instance_name)
    return galaxy.GalaxyInstance(conf[instance_name]['url'],
                                 conf[instance_name]['key'])

def get_toolshed_instance(instance_name=None):
    conf = get_instance(instance_name=instance_name)
    return toolshed.ToolShedInstance(conf[instance_name]['url'],
                                     conf[instance_name]['key'])
