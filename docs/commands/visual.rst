visual
======

This section is auto-generated from the help text for the parsec command
``visual``.


``get_visualizations`` command
------------------------------

**Usage**::

    parsec visual get_visualizations [OPTIONS]

**Help**

Get the list of all visualizations.


**Output**


    A list of dicts with details on individual visualizations.
     For example::

       [{'dbkey': 'eschColi_K12',
         'id': 'df1c7c96fc427c2d',
         'title': 'AVTest1',
         'type': 'trackster',
         'url': '/api/visualizations/df1c7c96fc427c2d'},
        {'dbkey': 'mm9',
         'id': 'a669f50f8bf55b02',
         'title': 'Bam to Bigwig',
         'type': 'trackster',
         'url': '/api/visualizations/a669f50f8bf55b02'}]
    
**Options**::


      -h, --help  Show this message and exit.
    

``show_visualization`` command
------------------------------

**Usage**::

    parsec visual show_visualization [OPTIONS] VISUAL_ID

**Help**

Get details of a given visualization.


**Output**


    A description of the given visualization.
     For example::

       {'annotation': None,
        'dbkey': 'mm9',
        'id': '18df9134ea75e49c',
        'latest_revision': {  ... },
        'model_class': 'Visualization',
        'revisions': ['aa90649bb3ec7dcb', '20622bc6249c0c71'],
        'slug': 'visualization-for-grant-1',
        'title': 'Visualization For Grant',
        'type': 'trackster',
        'url': '/u/azaron/v/visualization-for-grant-1',
        'user_id': '21e4aed91386ca8b'}
    
**Options**::


      -h, --help  Show this message and exit.
    
