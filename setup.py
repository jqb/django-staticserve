from setuptools import setup, find_packages

setup(
    name='django-staticserve',
    version='1.0',
    description='Simple & resusable django utility that makes serving static files in debug mode painless.',
    author='Kuba Janoszek',
    author_email='kuba.janoszek@gmail.com',
    url='http://github.com/jqb/django-staticserve/tree/master',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    setup_requires=['setuptools_git'],
    zip_safe=False,
)
