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

       [{u'dbkey': u'eschColi_K12',
         u'id': u'df1c7c96fc427c2d',
         u'title': u'AVTest1',
         u'type': u'trackster',
         u'url': u'/api/visualizations/df1c7c96fc427c2d'},
        {u'dbkey': u'mm9',
         u'id': u'a669f50f8bf55b02',
         u'title': u'Bam to Bigwig',
         u'type': u'trackster',
         u'url': u'/api/visualizations/a669f50f8bf55b02'}]
    
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

       {u'annotation': None,
        u'dbkey': u'mm9',
        u'id': u'18df9134ea75e49c',
        u'latest_revision': {  ... },
        u'model_class': u'Visualization',
        u'revisions': [u'aa90649bb3ec7dcb', u'20622bc6249c0c71'],
        u'slug': u'visualization-for-grant-1',
        u'title': u'Visualization For Grant',
        u'type': u'trackster',
        u'url': u'/u/azaron/v/visualization-for-grant-1',
        u'user_id': u'21e4aed91386ca8b'}
    
**Options**::


      -h, --help  Show this message and exit.
    
