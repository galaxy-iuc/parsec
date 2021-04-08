.. :changelog:

History
=======

.. to_doc

----------------------
1.15.0 (2021-04-08)
----------------------

* Update bioblend to 0.15.0

----------------------
1.13.0 (2019-08-12)
----------------------

* Multiple bugfixes
* Update bioblend to 0.13.0

----------------------
1.12.1 (2019-04-29)
----------------------

* Fix missing ``json_loads``


----------------------
1.12.0 (2019-04-10)
----------------------

* Update to bioblend 0.12.0, and pin to prevent version issues with hardcoded parsec calls
* Remove ``wait_for_completion`` (Thanks `@andreyto <https://github.com/andreyto>`__, `#24 <https://github.com/galaxy-iuc/parsec/pull/24>`__)

----------------------
1.0.6 (2018-12-13)
----------------------

* Fix a bug in json_loading (Thanks `@abretaud <https://github.com/abretaud>`__)
* Miscellaneous other command-engine bug

----------------------
1.0.5 (2018-10-03)
----------------------

* Update to latest bioblend fixing ``download_dataset``
* Rebuild documentation for new bioblend

----------------------
1.0.4 (2017-09-11)
----------------------

* Correct documentation quoting for ZSH (Thanks `@manabuishii <https://github.com/manabuishii>`__)
* New and improved error handling (Thanks `@abretaud <https://github.com/abretaud>`__)

----------------------
1.0.3-rc1 (2017-06-27)
----------------------

* Add toolshed support to parsec

----------------------
1.0.2 (2017-06-12)
----------------------

* Support configuration files from alternate locations (Thanks `@manabuishii <https://github.com/manabuishii>`__)
* Support specifying galaxy url / api key on command line (Thanks `@manabuishii <https://github.com/manabuishii>`__)

----------------------
1.0.1 (2017-05-26)
----------------------

* Fix small issue with installation

----------------------
1.0.0 (2017-05-26)
----------------------

* New utilities for xunit xargs and waiting on a workflow to complete
* Support for quota API, and other new bioblend operations.
* Even more updated help

----------------------
1.0.0.rc1 (2017-05-03)
----------------------

* Updates to auto-builder
* Updated help
* New routes
* Subcommands instead of top-level commands

----------------------
0.9.rc2 (2015-03-05)
----------------------

* Removed lingering references to options.py preventing other users from using it
* Fixed bugs in auto-builder script

----------------------
0.9.rc1 (2015-03-02)
----------------------

* Implemented script to automatically build all wrappers from BioBlend's codebase

