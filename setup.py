#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os

from setuptools import setup

base_dir = os.path.dirname(__file__)

with codecs.open(os.path.join(base_dir, 'README.rst'), 'r', encoding='utf8') as f:
    long_description = f.read()

about = {}
with open(os.path.join(base_dir, 'djhuey_email', '__about__.py')) as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__summary__'],
    long_description=long_description,
    license=about['__license__'],
    url=about['__uri__'],
    author=about['__author__'],
    author_email=about['__email__'],
    platforms=['any'],
    packages=['djhuey_email'],
    scripts=[],
    zip_safe=False,
    install_requires=[
        'huey>=1.10.2'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.+',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Operating System :: POSIX',
        'Topic :: Communications',
        'Topic :: Communications :: Email',
        'Topic :: System :: Distributed Computing',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
