spcrawler: a command-line tool to backup Sharepoint public installation data from open API endpoint
########################################################################################################################

spcrawler is a command-line tool to backup Sharepoint public installation data from open API endpoint
It uses Sharepoint API located at "/_api/web" and dumps all data and resources.


.. contents::

.. section-numbering::



Main features
=============

* Metadata extraction
* Download all files (resources) from Sharepoint installation



Installation
============


Any OS
-------------

A universal installation method (that works on Windows, Mac OS X, Linux, …,
and always provides the latest version) is to use pip:


.. code-block:: bash

    # Make sure we have an up-to-date version of pip and setuptools:
    $ pip install --upgrade pip setuptools

    $ pip install --upgrade spcrawler


(If ``pip`` installation fails for some reason, you can try
``easy_install spcrawler`` as a fallback.)


Python version
--------------

Python version 3.6 or greater is required.

Usage
=====


Synopsis:

.. code-block:: bash

    $ spcrawler [command] [flags]


See also ``python -m spcrawler`` and ``spcrawler [command] --help`` for help for each command.



Commands
========

Ping command
------------
Pings API endpoint located at url + "/_api/web" and returns OK if it's available.


Ping asutk.ru API endpoint

.. code-block:: bash

    $ spcrawler ping --url https://asutk.ru



Walk command
------------
Lists objects in Sharepoint installation

Walks over FA.ru website objects

.. code-block:: bash

    $ spcrawler walk --url http://fa.ru

Dump command
------------
Dumps all objects/lists/data from API to JSON lines files. Stores all data to local path "domainname/data"

Dumps data from FA.ru (Financial university) website

.. code-block:: bash

    $ spcrawler dump --url http://fa.ru

