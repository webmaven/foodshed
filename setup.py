# -*- coding: utf-8 -*-
"""Setup script."""

import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name='foodshed',
    version='0.1',
    author="Michael R. Bernstein",
    author_email="michaelb@codeforamerica.org",
    description=("The DC Foodshed App"),
    long_description=(
        read('README.rst')
        + '\n\n' +
        read('CHANGES.rst')
        ),
    license="GNU AGPLv3",
    keywords="bobo gae appengine food map",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
        ],
    url='',
    packages=find_packages(),
    package_dir = {'': os.sep.join(['src', 'dcfoodshed'])},
    include_package_data=True,
    install_requires=[
        'bobo',
        'chameleon',
        'distribute',
        'geomodel'
    ],
    zip_safe=False,
)
