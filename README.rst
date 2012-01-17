django-staticserve
******************

Simple & resusable django utility that makes
serving static files in debug mode painless.

For some reasons django's own solutions for
serving static files does not work as expected,
so I've created this package.


Usage
-----

Package provides two middleware classes

- `staticserve.middleware.StaticServe`
  uses STATIC_URL & STATIC_ROOT settings

- `staticserve.middleware.MediaServe`
  uses MEDIA_URL & MEDIA_ROOT settings


To use it just put in your projects MIDDLEWARE_CLASSES settings::

  MIDDLEWARE_CLASSES = (
      # ...
      'staticserve.middleware.StaticServe',

      # OR:
      # 'staticserve.middleware.StaticServe',
  )


Depending where you keep static files.
It works only if DEBUG == True.


Installation
------------

simply download and install::

  python setup.py install

or directly from github::

  pip install -e git+git@github.com:jqb/django-staticserve.git#egg=staticserve
