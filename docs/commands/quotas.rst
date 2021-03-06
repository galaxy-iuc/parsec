quotas
======

This section is auto-generated from the help text for the parsec command
``quotas``.


``create_quota`` command
------------------------

**Usage**::

    parsec quotas create_quota [OPTIONS] NAME DESCRIPTION AMOUNT OPERATION

**Help**

Create a new quota


**Output**


    A description of quota.
     For example::

       {u'url': '/galaxy/api/quotas/386f14984287a0f7',
        u'model_class': 'Quota',
        u'message': "Quota 'Testing' has been created with 1 associated users and 0 associated groups.",
        u'id': '386f14984287a0f7',
        u'name': 'Testing'}
    
**Options**::


      --default TEXT    Whether or not this is a default quota. Valid values are
                        ``no``, ``unregistered``, ``registered``. None is equivalent
                        to ``no``.  [default: no]
      --in_users TEXT   A list of user IDs or user emails.
      --in_groups TEXT  A list of group IDs or names.
      -h, --help        Show this message and exit.
    

``delete_quota`` command
------------------------

**Usage**::

    parsec quotas delete_quota [OPTIONS] QUOTA_ID

**Help**

Delete a quota


**Output**


    A description of the changes, mentioning the deleted quota.
     For example::

       "Deleted 1 quotas: Testing-B"
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_quotas`` command
----------------------

**Usage**::

    parsec quotas get_quotas [OPTIONS]

**Help**

Get a list of quotas


**Output**


    A list of dicts with details on individual quotas.
     For example::

       [{u'id': u'0604c8a56abe9a50',
         u'model_class': u'Quota',
         u'name': u'test ',
         u'url': u'/api/quotas/0604c8a56abe9a50'},
        {u'id': u'1ee267091d0190af',
         u'model_class': u'Quota',
         u'name': u'workshop',
         u'url': u'/api/quotas/1ee267091d0190af'}]
    
**Options**::


      --deleted   Only return quota(s) that have been deleted
      -h, --help  Show this message and exit.
    

``show_quota`` command
----------------------

**Usage**::

    parsec quotas show_quota [OPTIONS] QUOTA_ID

**Help**

Display information on a quota


**Output**


    A description of quota.
     For example::

       {u'bytes': 107374182400,
        u'default': [],
        u'description': u'just testing',
        u'display_amount': u'100.0 GB',
        u'groups': [],
        u'id': u'0604c8a56abe9a50',
        u'model_class': u'Quota',
        u'name': u'test ',
        u'operation': u'=',
        u'users': []}
    
**Options**::


      --deleted   Search for quota in list of ones already marked as deleted
      -h, --help  Show this message and exit.
    

``undelete_quota`` command
--------------------------

**Usage**::

    parsec quotas undelete_quota [OPTIONS] QUOTA_ID

**Help**

Undelete a quota


**Output**


    A description of the changes, mentioning the undeleted quota.
     For example::

       "Undeleted 1 quotas: Testing-B"
    
**Options**::


      -h, --help  Show this message and exit.
    

``update_quota`` command
------------------------

**Usage**::

    parsec quotas update_quota [OPTIONS] QUOTA_ID

**Help**

Update an existing quota


**Output**


    A semicolon separated list of changes to the quota.
     For example::

       "Quota 'Testing-A' has been renamed to 'Testing-B'; Quota 'Testing-e' is now '-100.0 GB'; Quota 'Testing-B' is now the default for unregistered users"
    
**Options**::


      --name TEXT         Name for the new quota. This must be unique within a
                          Galaxy instance.
      --description TEXT  Quota description. If you supply this parameter, but not
                          the name, an error will be thrown.
      --amount TEXT       Quota size (E.g. ``10000MB``, ``99 gb``, ``0.2T``,
                          ``unlimited``)
      --operation TEXT    One of (``+``, ``-``, ``=``). If you wish to change this
                          value, you must also provide the ``amount``, otherwise it
                          will not take effect.
      --default TEXT      Whether or not this is a default quota. Valid values are
                          ``no``, ``unregistered``, ``registered``. Calling this
                          method with ``default="no"`` on a non-default quota will
                          throw an error. Not passing this parameter is equivalent
                          to passing ``no``.  [default: no]
      --in_users TEXT     A list of user IDs or user emails.
      --in_groups TEXT    A list of group IDs or names.
      -h, --help          Show this message and exit.
    
