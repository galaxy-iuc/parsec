libraries
=========

This section is auto-generated from the help text for the parsec command
``libraries``.


``copy_from_dataset`` command
-----------------------------

**Usage**::

    parsec libraries copy_from_dataset [OPTIONS] LIBRARY_ID DATASET_ID

**Help**

Copy a Galaxy dataset into a library.


**Output**


    LDDA information
    
**Options**::


      --folder_id TEXT  id of the folder where to place the uploaded files. If not
                        provided, the root folder will be used
    
      --message TEXT    message for copying action
      -h, --help        Show this message and exit.
    

``create_folder`` command
-------------------------

**Usage**::

    parsec libraries create_folder [OPTIONS] LIBRARY_ID FOLDER_NAME

**Help**

Create a folder in a library.


**Output**


    List with a single dictionary containing information about the new folder
    
**Options**::


      --description TEXT     description of the new folder in the data library
      --base_folder_id TEXT  id of the folder where to create the new folder. If not
                             provided, the root folder will be used
    
      -h, --help             Show this message and exit.
    

``create_library`` command
--------------------------

**Usage**::

    parsec libraries create_library [OPTIONS] NAME

**Help**

Create a data library with the properties defined in the arguments.


**Output**


    Details of the created library.
     For example::

       {'id': 'f740ab636b360a70',
        'name': 'Library from bioblend',
        'url': '/api/libraries/f740ab636b360a70'}
    
**Options**::


      --description TEXT  Optional data library description
      --synopsis TEXT     Optional data library synopsis
      -h, --help          Show this message and exit.
    

``delete_library`` command
--------------------------

**Usage**::

    parsec libraries delete_library [OPTIONS] LIBRARY_ID

**Help**

Delete a data library.


**Output**


    Information about the deleted library

   .. warning::
     Deleting a data library is irreversible - all of the data from the
     library will be permanently deleted.
    
**Options**::


      -h, --help  Show this message and exit.
    

``delete_library_dataset`` command
----------------------------------

**Usage**::

    parsec libraries delete_library_dataset [OPTIONS] LIBRARY_ID DATASET_ID

**Help**

Delete a library dataset in a data library.


**Output**


    A dictionary containing the dataset id and whether the dataset
     has been deleted.
     For example::

       {'deleted': True,
        'id': '60e680a037f41974'}
    
**Options**::


      --purged    Indicate that the dataset should be purged (permanently deleted)
      -h, --help  Show this message and exit.
    

``get_dataset_permissions`` command
-----------------------------------

**Usage**::

    parsec libraries get_dataset_permissions [OPTIONS] DATASET_ID

**Help**

Get the permissions for a dataset.


**Output**


    dictionary with all applicable permissions' values
    
**Options**::


      -h, --help  Show this message and exit.
    

``get_folders`` command
-----------------------

**Usage**::

    parsec libraries get_folders [OPTIONS] LIBRARY_ID

**Help**

Get all the folders in a library, or select a subset by specifying a folder name for filtering.


**Output**


    list of dicts each containing basic information about a folder
    
**Options**::


      --folder_id TEXT  filter for folder by folder id
      --name TEXT       Folder name to filter on. For ``name`` specify the full path
                        of the folder starting from the library's root folder, e.g.
                        ``/subfolder/subsubfolder``.
    
      -h, --help        Show this message and exit.
    

``get_libraries`` command
-------------------------

**Usage**::

    parsec libraries get_libraries [OPTIONS]

**Help**

Get all libraries, or select a subset by specifying optional arguments for filtering (e.g. a library name).


**Output**


    list of dicts each containing basic information about a library
    
**Options**::


      --library_id TEXT  filter for library by library id
      --name TEXT        Library name to filter on.
      --deleted          If ``False`` (the default), return only non-deleted
                         libraries. If ``True``, return only deleted libraries. If
                         ``None``, return both deleted and non-deleted libraries.
    
      -h, --help         Show this message and exit.
    

``get_library_permissions`` command
-----------------------------------

**Usage**::

    parsec libraries get_library_permissions [OPTIONS] LIBRARY_ID

**Help**

Get the permissions for a library.


**Output**


    dictionary with all applicable permissions' values
    
**Options**::


      -h, --help  Show this message and exit.
    

``set_dataset_permissions`` command
-----------------------------------

**Usage**::

    parsec libraries set_dataset_permissions [OPTIONS] DATASET_ID

**Help**

Set the permissions for a dataset. Note: it will override all security for this dataset even if you leave out a permission type.


**Output**


    dictionary with all applicable permissions' values
    
**Options**::


      --access_in TEXT  list of role ids
      --modify_in TEXT  list of role ids
      --manage_in TEXT  list of role ids
      -h, --help        Show this message and exit.
    

``set_library_permissions`` command
-----------------------------------

**Usage**::

    parsec libraries set_library_permissions [OPTIONS] LIBRARY_ID

**Help**

Set the permissions for a library. Note: it will override all security for this library even if you leave out a permission type.


**Output**


    General information about the library
    
**Options**::


      --access_in TEXT  list of role ids
      --modify_in TEXT  list of role ids
      --add_in TEXT     list of role ids
      --manage_in TEXT  list of role ids
      -h, --help        Show this message and exit.
    

``show_dataset`` command
------------------------

**Usage**::

    parsec libraries show_dataset [OPTIONS] LIBRARY_ID DATASET_ID

**Help**

Get details about a given library dataset. The required ``library_id`` can be obtained from the datasets's library content details.


**Output**


    A dictionary containing information about the dataset in the
     library
    
**Options**::


      -h, --help  Show this message and exit.
    

``show_folder`` command
-----------------------

**Usage**::

    parsec libraries show_folder [OPTIONS] LIBRARY_ID FOLDER_ID

**Help**

Get details about a given folder. The required ``folder_id`` can be obtained from the folder's library content details.


**Output**


    Information about the folder
    
**Options**::


      -h, --help  Show this message and exit.
    

``show_library`` command
------------------------

**Usage**::

    parsec libraries show_library [OPTIONS] LIBRARY_ID

**Help**

Get information about a library.


**Output**


    details of the given library
    
**Options**::


      --contents  whether to get contents of the library (rather than just the
                  library details)
    
      -h, --help  Show this message and exit.
    

``update_library_dataset`` command
----------------------------------

**Usage**::

    parsec libraries update_library_dataset [OPTIONS] DATASET_ID

**Help**

Update library dataset metadata. Some of the attributes that can be modified are documented below.


**Output**


    details of the updated dataset
    
**Options**::


      --file_ext TEXT      Replace library dataset extension (must exist in the
                           Galaxy registry)
    
      --genome_build TEXT  Replace library dataset genome build (dbkey)
      --misc_info TEXT     Replace library dataset misc_info with given string
      --name TEXT          Replace library dataset name with the given string
      --tags TEXT          Replace library dataset tags with the given list
      -h, --help           Show this message and exit.
    

``upload_file_contents`` command
--------------------------------

**Usage**::

    parsec libraries upload_file_contents [OPTIONS] LIBRARY_ID PASTED_CONTENT

**Help**

Upload pasted_content to a data library as a new file.


**Output**


    List with a single dictionary containing information about the LDDA
    
**Options**::


      --folder_id TEXT  id of the folder where to place the uploaded file. If not
                        provided, the root folder will be used
    
      --file_type TEXT  Galaxy file format name  [default: auto]
      --dbkey TEXT      Dbkey  [default: ?]
      --tags TEXT       A list of tags to add to the datasets
      -h, --help        Show this message and exit.
    

``upload_file_from_local_path`` command
---------------------------------------

**Usage**::

    parsec libraries upload_file_from_local_path [OPTIONS] LIBRARY_ID

**Help**

Read local file contents from file_local_path and upload data to a library.


**Output**


    List with a single dictionary containing information about the LDDA
    
**Options**::


      --folder_id TEXT  id of the folder where to place the uploaded file. If not
                        provided, the root folder will be used
    
      --file_type TEXT  Galaxy file format name  [default: auto]
      --dbkey TEXT      Dbkey  [default: ?]
      --tags TEXT       A list of tags to add to the datasets
      -h, --help        Show this message and exit.
    

``upload_file_from_server`` command
-----------------------------------

**Usage**::

    parsec libraries upload_file_from_server [OPTIONS] LIBRARY_ID SERVER_DIR

**Help**

Upload all files in the specified subdirectory of the Galaxy library import directory to a library.


**Output**


    List with a single dictionary containing information about the LDDA
    
**Options**::


      --folder_id TEXT       id of the folder where to place the uploaded files. If
                             not provided, the root folder will be used
    
      --file_type TEXT       Galaxy file format name  [default: auto]
      --dbkey TEXT           Dbkey  [default: ?]
      --link_data_only TEXT  either 'copy_files' (default) or 'link_to_files'.
                             Setting to 'link_to_files' symlinks instead of copying
                             the files
    
      --roles TEXT           ???
      --preserve_dirs        Indicate whether to preserve the directory structure
                             when importing dir
    
      --tag_using_filenames  Indicate whether to generate dataset tags from
                             filenames.
    
      --tags TEXT            A list of tags to add to the datasets
      -h, --help             Show this message and exit.
    

``upload_file_from_url`` command
--------------------------------

**Usage**::

    parsec libraries upload_file_from_url [OPTIONS] LIBRARY_ID FILE_URL

**Help**

Upload a file to a library from a URL.


**Output**


    List with a single dictionary containing information about the LDDA
    
**Options**::


      --folder_id TEXT  id of the folder where to place the uploaded file. If not
                        provided, the root folder will be used
    
      --file_type TEXT  Galaxy file format name  [default: auto]
      --dbkey TEXT      Dbkey  [default: ?]
      --tags TEXT       A list of tags to add to the datasets
      -h, --help        Show this message and exit.
    

``upload_from_galaxy_filesystem`` command
-----------------------------------------

**Usage**::

    parsec libraries upload_from_galaxy_filesystem [OPTIONS] LIBRARY_ID

**Help**

Upload a set of files already present on the filesystem of the Galaxy server to a library.


**Output**


    List with a single dictionary containing information about the LDDA
    
**Options**::


      --folder_id TEXT       id of the folder where to place the uploaded files. If
                             not provided, the root folder will be used
    
      --file_type TEXT       Galaxy file format name  [default: auto]
      --dbkey TEXT           Dbkey  [default: ?]
      --link_data_only TEXT  either 'copy_files' (default) or 'link_to_files'.
                             Setting to 'link_to_files' symlinks instead of copying
                             the files
    
      --roles TEXT           ???
      --preserve_dirs        Indicate whether to preserve the directory structure
                             when importing dir
    
      --tag_using_filenames  Indicate whether to generate dataset tags from
                             filenames.
    
      --tags TEXT            A list of tags to add to the datasets
      -h, --help             Show this message and exit.
    

``wait_for_dataset`` command
----------------------------

**Usage**::

    parsec libraries wait_for_dataset [OPTIONS] LIBRARY_ID DATASET_ID

**Help**

Wait until the library dataset state is terminal ('ok', 'empty', 'error', 'discarded' or 'failed_metadata').


**Output**


    A dictionary containing information about the dataset in the
     library
    
**Options**::


      --maxwait FLOAT   Total time (in seconds) to wait for the dataset state to
                        become terminal. If the dataset state is not terminal within
                        this time, a ``DatasetTimeoutException`` will be thrown.
                        [default: 12000]
    
      --interval FLOAT  Time (in seconds) to wait between 2 consecutive checks.
                        [default: 3]
    
      -h, --help        Show this message and exit.
    
