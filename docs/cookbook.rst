========
Cookbook
========

This page will contain more easy "recipes" for using parsec as time goes
on. Short tips and tricks that can help you use it more effectively, or
short recipes that can document how to do more complex tasks.

Talking to multiple Galaxies
----------------------------

If you are regularly switching between multiple Galaxy instances, you'll
probably want to take advantage of the environment variable for
specifying a Galaxy instance. E.g.:

.. code-block:: shell

    $ PARSEC_GALAXY_INSTANCE=uni-admin parsec config get_config | jq .brand
    "Internal"
    $ PARSEC_GALAXY_INSTANCE=uni-public parsec config get_config | jq .brand
    "Public"

You could easily set these at the top of a parsec script you've built
and all commands from there on would talk to the same Galaxy instance.
