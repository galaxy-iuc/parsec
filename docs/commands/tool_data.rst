tool_data
=========

This section is auto-generated from the help text for the parsec command
``tool_data``.


``delete_data_table`` command
-----------------------------

**Usage**::

    parsec tool_data delete_data_table [OPTIONS] DATA_TABLE_ID VALUES

**Help**

Delete an item from a data table.


**Output**


    
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_data_tables`` command
---------------------------

**Usage**::

    parsec tool_data get_data_tables [OPTIONS]

**Help**

Get the list of all data tables.


**Output**


    A list of dicts with details on individual data tables.
     For example::

       [{"model_class": "TabularToolDataTable", "name": "fasta_indexes"},
        {"model_class": "TabularToolDataTable", "name": "bwa_indexes"}]
    
**Options**::


      -h, --help  Show this message and exit.
    

``reload_data_table`` command
-----------------------------

**Usage**::

    parsec tool_data reload_data_table [OPTIONS] DATA_TABLE_ID

**Help**

Reload a data table.


**Output**


    A description of the given data table and its content.
     For example::

       {"columns": ["value", "dbkey", "name", "path"],
        "fields": [["test id",
          "test",
          "test name",
          "/opt/galaxy-dist/tool-data/test/seq/test id.fa"]],
        "model_class": "TabularToolDataTable",
        "name": "all_fasta"}
    
**Options**::


      -h, --help  Show this message and exit.
    

``show_data_table`` command
---------------------------

**Usage**::

    parsec tool_data show_data_table [OPTIONS] DATA_TABLE_ID

**Help**

Get details of a given data table.


**Output**


    A description of the given data table and its content.
     For example::

       {"columns": ["value", "dbkey", "name", "path"],
        "fields": [["test id",
          "test",
          "test name",
          "/opt/galaxy-dist/tool-data/test/seq/test id.fa"]],
        "model_class": "TabularToolDataTable",
        "name": "all_fasta"}
    
**Options**::


      -h, --help  Show this message and exit.
    
