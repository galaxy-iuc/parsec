users
=====

``create_local_user`` command
-----------------------------

This section is auto-generated from the help text for the parsec command
``users``.

**Usage**::

    parsec users create_local_user [OPTIONS] USERNAME USER_EMAIL PASSWORD

**Help**

Create a new Galaxy local user.

**Options**::


      -h, --help  Show this message and exit.
    

``create_remote_user`` command
------------------------------

This section is auto-generated from the help text for the parsec command
``users``.

**Usage**::

    parsec users create_remote_user [OPTIONS] USER_EMAIL

**Help**

Create a new Galaxy remote user.

**Options**::


      -h, --help  Show this message and exit.
    

``create_user`` command
-----------------------

This section is auto-generated from the help text for the parsec command
``users``.

**Usage**::

    parsec users [OPTIONS] COMMAND [ARGS]...

**Help**

Deprecated method.


``create_user_apikey`` command
------------------------------

This section is auto-generated from the help text for the parsec command
``users``.

**Usage**::

    parsec users create_user_apikey [OPTIONS] USER_ID

**Help**

Create a new API key for a given user.

**Options**::


      -h, --help  Show this message and exit.
    

``delete_user`` command
-----------------------

This section is auto-generated from the help text for the parsec command
``users``.

**Usage**::

    parsec users delete_user [OPTIONS] USER_ID

**Help**

Delete a user.

**Options**::


      --purge     if ``True``, also purge (permanently delete) the history
      -h, --help  Show this message and exit.
    

``get_current_user`` command
----------------------------

This section is auto-generated from the help text for the parsec command
``users``.

**Usage**::

    parsec users get_current_user [OPTIONS]

**Help**

Display information about the user associated with this Galaxy connection.

**Options**::


      -h, --help  Show this message and exit.
    

``get_users`` command
---------------------

This section is auto-generated from the help text for the parsec command
``users``.

**Usage**::

    parsec users get_users [OPTIONS]

**Help**

Get a list of all registered users. If ``deleted`` is set to ``True``, get a list of deleted users.

**Options**::


      --deleted TEXT
      -h, --help      Show this message and exit.
    

``show_user`` command
---------------------

This section is auto-generated from the help text for the parsec command
``users``.

**Usage**::

    parsec users show_user [OPTIONS] USER_ID

**Help**

Display information about a user.

**Options**::


      --deleted   whether to return results for a deleted user
      -h, --help  Show this message and exit.
    
