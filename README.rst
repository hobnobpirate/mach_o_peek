.. highlight:: shell

===========
Mach-O Peek
===========

Package to examine parts of the Mach-O file. Purely academic and not for operational use at this time.

* Free software: MIT license


Features
--------

* TODO


Installation
------------

From sources
************

The sources for Mach-O Peek can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/hobnobpirate/mach_o_peek

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/hobnobpirate/mach_o_peek/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install

Script will be installed as mach-o-peek and can be run within the (virtual) environment in which you installed it:

.. code-block:: console

    $ mach-o-peek --help


.. _Github repo: https://github.com/hobnobpirate/mach_o_peek
.. _tarball: https://github.com/hobnobpirate/mach_o_peek/tarball/master


Usage
-----

* do things

Mach-O Resources
----------------

A webibliography of sites related to Mach-O used when building this application.

https://lowlevelbits.org/parsing-mach-o-files/

http://opensource.apple.com//source/xnu/xnu-1456.1.26/EXTERNAL_HEADERS/mach-o/loader.h

https://opensource.apple.com/source/xnu/xnu-4570.41.2/osfmk/mach/machine.h.auto.html

https://web.archive.org/web/20090901205800/http://developer.apple.com/mac/library/documentation/DeveloperTools/Conceptual/MachORuntime/Reference/reference.html

https://www.objc.io/issues/6-build-tools/mach-o-executables/

https://github.com/aidansteele/osx-abi-macho-file-format-reference

https://github.com/kaitai-io/kaitai_struct_formats/blob/master/executable/mach_o.ksy


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
