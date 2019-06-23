.. highlight:: shell

===========
Mach-O Peek
===========

Package to examine parts of the Mach-O file.
Purely academic and not for operational use at this time.
Similar functionality to :shell:`otool -h BINARY`.

* Free software: MIT license


Features
--------

* Reads header from executable

* Looks for 64-bit Mach O executable file format

* Extracts header attributes


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

Script will be installed as `mach-o-peek`.


Usage
-----

.. code-block:: console

    $ mach-o-peek --help


Mach-O Resources
----------------

* `Parsing Mach O Files`_

* `loader.h`_

* `machine.h`_

* `MachORunTime`_

* `Mach O Executables`_

* `OSX ABI MachO File Format Reference`_

* `Kaitai Mach O`_


Credits
-------

This package was created with Cookiecutter_ and
the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _Github repo: https://github.com/hobnobpirate/mach_o_peek
.. _tarball: https://github.com/hobnobpirate/mach_o_peek/tarball/master
.. _Parsing Mach O Files: https://lowlevelbits.org/parsing-mach-o-files/
.. _loader.h: http://opensource.apple.com//source/xnu/xnu-1456.1.26/EXTERNAL_HEADERS/mach-o/loader.h
.. _machine.h: https://opensource.apple.com/source/xnu/xnu-4570.41.2/osfmk/mach/machine.h.auto.html
.. _MachORunTime: https://web.archive.org/web/20090901205800/http://developer.apple.com/mac/library/documentation/DeveloperTools/Conceptual/MachORuntime/Reference/reference.html
.. _Mach O Executables: https://www.objc.io/issues/6-build-tools/mach-o-executables/
.. _OSX ABI MachO File Format Reference: https://github.com/aidansteele/osx-abi-macho-file-format-reference
.. _Kaitai Mach O: https://github.com/kaitai-io/kaitai_struct_formats/blob/master/executable/mach_o.ksy
