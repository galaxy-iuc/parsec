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


    Unique url of newly created form with encoded id
    
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

       [{u'id': u'f2db41e1fa331b3e',
         u'model_class': u'FormDefinition',
         u'name': u'First form',
         u'url': u'/api/forms/f2db41e1fa331b3e'},
        {u'id': u'ebfb8f50c6abde6d',
         u'model_class': u'FormDefinition',
         u'name': u'second form',
         u'url': u'/api/forms/ebfb8f50c6abde6d'}]
    
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

       {u'desc': u'here it is ',
        u'fields': [],
        u'form_definition_current_id': u'f2db41e1fa331b3e',
        u'id': u'f2db41e1fa331b3e',
        u'layout': [],
        u'model_class': u'FormDefinition',
        u'name': u'First form',
        u'url': u'/api/forms/f2db41e1fa331b3e'}
    
**Options**::


      -h, --help  Show this message and exit.
    
