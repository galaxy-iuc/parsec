roles
=====

This section is auto-generated from the help text for the parsec command
``roles``.


``create_role`` command
-----------------------

**Usage**::

    parsec roles create_role [OPTIONS] ROLE_NAME DESCRIPTION

**Help**

Create a new role.


**Output**


A (size 1) list with newly created role
     details, like::

       [{u'description': u'desc',
         u'url': u'/api/roles/ebfb8f50c6abde6d',
         u'model_class': u'Role',
         u'type': u'admin',
         u'id': u'ebfb8f50c6abde6d',
         u'name': u'Foo'}]
   
    
**Options**::


      --user_ids TEXT   A list of encoded user IDs to add to the new role
      --group_ids TEXT  A list of encoded group IDs to add to the new role
      -h, --help        Show this message and exit.
    

``get_roles`` command
---------------------

**Usage**::

    parsec roles get_roles [OPTIONS]

**Help**

Displays a collection (list) of roles.


**Output**


A list of dicts with details on individual roles.
     For example::

       [{"id": "f2db41e1fa331b3e",
         "model_class": "Role",
         "name": "Foo",
         "url": "/api/roles/f2db41e1fa331b3e"},
        {"id": "f597429621d6eb2b",
         "model_class": "Role",
         "name": "Bar",
         "url": "/api/roles/f597429621d6eb2b"}]
   
    
**Options**::


      -h, --help  Show this message and exit.
    

``show_role`` command
---------------------

**Usage**::

    parsec roles show_role [OPTIONS] ROLE_ID

**Help**

Display information on a single role


**Output**


A description of role
     For example::

       {"description": "Private Role for Foo",
        "id": "f2db41e1fa331b3e",
        "model_class": "Role",
        "name": "Foo",
        "type": "private",
        "url": "/api/roles/f2db41e1fa331b3e"}
   
    
**Options**::


      -h, --help  Show this message and exit.
    
