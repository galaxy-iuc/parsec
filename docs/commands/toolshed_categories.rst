toolshed_categories
===================

This section is auto-generated from the help text for the parsec command
``toolshed_categories``.


``get_categories`` command
--------------------------

**Usage**::

    parsec toolshed_categories get_categories [OPTIONS]

**Help**

Returns a list of dictionaries that contain descriptions of the repository categories found on the given Tool Shed instance.


**Output**


    A list of dictionaries containing information about
     repository categories present in the Tool Shed.
     For example::

       [{'deleted': False,
         'description': 'Tools for manipulating data',
         'id': '175812cd7caaf439',
         'model_class': 'Category',
         'name': 'Text Manipulation',
         'url': '/api/categories/175812cd7caaf439'}]

   .. versionadded:: 0.5.2
    
**Options**::


      --deleted   whether to show deleted categories
      -h, --help  Show this message and exit.
    

``show_category`` command
-------------------------

**Usage**::

    parsec toolshed_categories show_category [OPTIONS] CATEGORY_ID

**Help**

Get details of a given category.


**Output**


    details of the given category
    
**Options**::


      -h, --help  Show this message and exit.
    
