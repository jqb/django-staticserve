django-staticserve
******************

Simple & resusable django utility that makes
serving static files in debug mode painless.

For some reasons django's own solutions for
serving static files does not work as expected,
so I've created this package.


Usage
-----

Just put in your projects MIDDLEWARE_CLASSES settings::

  MIDDLEWARE_CLASSES = (
      # ...
      'staticserve.middleware.StaticServe',
  )

And that's it.

It works only if DEBUG == True.


Installation
------------

simply download and install::

  python setup.py install
