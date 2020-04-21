Emended.com website
###################

This is the source for `emended.com website <https://emended.com>`__.


Publishing
==========

Use ``bin/make-dist.sh <base-url>`` to generate the site using production
settings in the ``output`` directory. For example::

    bin/make-dist.sh https://emended.com

will generate the site for deployment at https://emended.com.

If <base-url> is https://emended.com or https://draft.emended.com site specific
configuration such as robots.txt will also be applied.

Publishing will use the following environment variables:

GOOGLE_ANALYTICS:
    Tracking code for Google analytics. If set, Google analytics will be
    enabled.


Development
===========

To install required python packages run::

    pip install -r requirements.txt

or::

    pip install --user -r requirements.txt

in the repository root.

Simply running ``pelican`` in the repository root will generate the site in the
``output`` directory. Note that the output directory will not be cleaned by
default -- use ``-d`` to also clean the output directory. ``-r`` flag is useful
for running the build automatically when input changes.

Useful command to run while developing is::

    SITEURL=http://localhost:8000 pelican -dr -s publishconf.py

using your own testing address which will also give you realistic canonical
urls etc. as in the production build.

Output can be served for development by using any simple http file server such as::

    python -m python -m http.server -b 127.0.0.1 8000``

The ``bin/serve-dev.sh`` helper does all the above i.e it serves the content
and runs Pelican in the continuous build mode.


Developing on Windows
=====================

Download latest Python installer for Windows and make sure you check "Add
python to PATH" when installing.

To install required Python packages, type::

    pip install -r requirements.txt

in the repository root. Now you should be able to use `pelican` command as
described in the previous section.
