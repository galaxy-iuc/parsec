users
=====

This section is auto-generated from the help text for the parsec command
``users``.


``create_local_user`` command
-----------------------------

**Usage**::

    parsec users create_local_user [OPTIONS] USERNAME USER_EMAIL PASSWORD

**Help**

Create a new Galaxy local user.


**Output**


    a dictionary containing information about the created user
    
**Options**::


      -h, --help  Show this message and exit.
    

``create_remote_user`` command
------------------------------

**Usage**::

    parsec users create_remote_user [OPTIONS] USER_EMAIL

**Help**

Create a new Galaxy remote user.


**Output**


    a dictionary containing information about the created user
    
**Options**::


      -h, --help  Show this message and exit.
    

``create_user_apikey`` command
------------------------------

**Usage**::

    parsec users create_user_apikey [OPTIONS] USER_ID

**Help**

Create a new API key for a given user.


**Output**


    the API key for the user
    
**Options**::


      -h, --help  Show this message and exit.
    

``delete_user`` command
-----------------------

**Usage**::

    parsec users delete_user [OPTIONS] USER_ID

**Help**

Delete a user.


**Output**


    a dictionary containing information about the deleted user
    
**Options**::


      --purge     if ``True``, also purge (permanently delete) the history
      -h, --help  Show this message and exit.
    

``get_current_user`` command
----------------------------

**Usage**::

    parsec users get_current_user [OPTIONS]

**Help**

Display information about the user associated with this Galaxy connection.


**Output**


    a dictionary containing information about the current user
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_user_apikey`` command
---------------------------

**Usage**::

    parsec users get_user_apikey [OPTIONS] USER_ID

**Help**

Get the current API key for a given user. This functionality is available since Galaxy ``release_17.01``.


**Output**


    the API key for the user
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_users`` command
---------------------

**Usage**::

    parsec users get_users [OPTIONS]

**Help**

Get a list of all registered users. If ``deleted`` is set to ``True``, get a list of deleted users.


**Output**


    a list of dicts with user details.
            For example::

              [{u'email': u'a_user@example.com',
                u'id': u'dda47097d9189f15',
                u'url': u'/api/users/dda47097d9189f15'}]
    
**Options**::


      --deleted       Whether to include deleted users
      --f_email TEXT  filter for user emails. The filter will be active for non-
                      admin users only if the Galaxy instance has the
                      ``expose_user_email`` option set to ``true`` in the
                      ``config/galaxy.yml`` configuration file. This parameter is
                      silently ignored for non-admin users in Galaxy
                      ``release_15.01`` and earlier.
      --f_name TEXT   filter for user names. The filter will be active for non-admin
                      users only if the Galaxy instance has the ``expose_user_name``
                      option set to ``true`` in the ``config/galaxy.yml``
                      configuration file. This parameter is silently ignored in
                      Galaxy ``release_15.10`` and earlier.
      --f_any TEXT    filter for user email or name. Each filter will be active for
                      non-admin users only if the Galaxy instance has the
                      corresponding ``expose_user_*`` option set to ``true`` in the
                      ``config/galaxy.yml`` configuration file. This parameter is
                      silently ignored in Galaxy ``release_15.10`` and earlier.
      -h, --help      Show this message and exit.
    

``show_user`` command
---------------------

**Usage**::

    parsec users show_user [OPTIONS] USER_ID

**Help**

Display information about a user.


**Output**


    a dictionary containing information about the user
    
**Options**::


      --deleted   whether to return results for a deleted user
      -h, --help  Show this message and exit.
    
