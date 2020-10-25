========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |
        |
    * - package
      - | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/gem_python/badge/?style=flat
    :target: https://readthedocs.org/projects/gem_python
    :alt: Documentation Status

.. |commits-since| image:: https://img.shields.io/github/commits-since/rebirthxi/gem_python/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/rebirthxi/gem_python/compare/v0.0.1...master



.. end-badges

A python package containing all the libraries needed for the python portion of the FFXI Server Emulator: "Shattered
Gem"

* Free software: MIT license

Installation
============

::

    pip install gem-python

You can also install the in-development version with::

    pip install https://github.com/rebirthxi/gem_python/archive/master.zip


Documentation
=============


https://gem_python.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
