forms
=====

This section is auto-generated from the help text for the parsec command
``forms``.


``create_form`` command
-----------------------

**Usage**::

    parsec forms create_form [OPTIONS] FORM_XML_TEXT

**Help**

Create a new form.


**Output**


    Unique URL of newly created form with encoded id

**Options**::


      -h, --help  Show this message and exit.


``get_forms`` command
---------------------

**Usage**::

    parsec forms get_forms [OPTIONS]

**Help**

Get the list of all forms.


**Output**


    Displays a collection (list) of forms.
     For example::

       [{'id': 'f2db41e1fa331b3e',
         'model_class': 'FormDefinition',
         'name': 'First form',
         'url': '/api/forms/f2db41e1fa331b3e'},
        {'id': 'ebfb8f50c6abde6d',
         'model_class': 'FormDefinition',
         'name': 'second form',
         'url': '/api/forms/ebfb8f50c6abde6d'}]

**Options**::


      -h, --help  Show this message and exit.


``show_form`` command
---------------------

**Usage**::

    parsec forms show_form [OPTIONS] FORM_ID

**Help**

Get details of a given form.


**Output**


    A description of the given form.
     For example::

       {'desc': 'here it is ',
        'fields': [],
        'form_definition_current_id': 'f2db41e1fa331b3e',
        'id': 'f2db41e1fa331b3e',
        'layout': [],
        'model_class': 'FormDefinition',
        'name': 'First form',
        'url': '/api/forms/f2db41e1fa331b3e'}

**Options**::


      -h, --help  Show this message and exit.

