dataset_collections
===================

This section is auto-generated from the help text for the parsec command
``dataset_collections``.


``download_dataset_collection`` command
---------------------------------------

**Usage**::

    parsec dataset_collections download_dataset_collection 

**Help**

Download a history dataset collection as an archive.


**Output**


    Information about the downloaded archive.

   .. note::
     This method downloads a ``zip`` archive for Galaxy 21.01 and later.
     For earlier versions of Galaxy this method downloads a ``tgz`` archive.
     This method is only supported by Galaxy 18.01 or later.
    
**Options**::


      -h, --help  Show this message and exit.
    

``show_dataset_collection`` command
-----------------------------------

**Usage**::

    parsec dataset_collections show_dataset_collection [OPTIONS]

**Help**

Get details of a given dataset collection of the current user


**Output**


    element view of the dataset collection
    
**Options**::


      --instance_type TEXT  instance type of the collection - 'history' or 'library'
                            [default: history]
    
      -h, --help            Show this message and exit.
    

``wait_for_dataset_collection`` command
---------------------------------------

**Usage**::

    parsec dataset_collections wait_for_dataset_collection 

**Help**

Wait until all or a specified proportion of elements of a dataset collection are in a terminal state.


**Output**


    Details of the given dataset collection.
    
**Options**::


      --maxwait FLOAT              Total time (in seconds) to wait for the dataset
                                   states in the dataset collection to become
                                   terminal. If not all datasets are in a terminal
                                   state within this time, a
                                   ``DatasetCollectionTimeoutException`` will be
                                   raised.  [default: 12000]
    
      --interval FLOAT             Time (in seconds) to wait between two consecutive
                                   checks.  [default: 3]
    
      --proportion_complete FLOAT  Proportion of elements in this collection that
                                   have to be in a terminal state for this method to
                                   return. Must be a number between 0 and 1. For
                                   example: if the dataset collection contains 2
                                   elements, and proportion_complete=0.5 is
                                   specified, then wait_for_dataset_collection will
                                   return as soon as 1 of the 2 datasets is in a
                                   terminal state. Default is 1, i.e. all elements
                                   must complete.  [default: 1.0]
    
      --check                      Whether to check if all the terminal states of
                                   datasets in the dataset collection are 'ok'. This
                                   will raise an Exception if a dataset is in a
                                   terminal state other than 'ok'.  [default: True]
    
      -h, --help                   Show this message and exit.
    
