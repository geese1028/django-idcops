# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import setuptools
from distutils.core import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def get_requirements():
    with open(os.path.join(os.path.dirname(__file__), "requirements.txt")) as f:
        requirements_list = [req.strip() for req in f.readlines()]
    return requirements_list


setup(
    name='django-idcops',
    version='2.0',
    packages=['idcops',
              'idcops.lib',
              'idcops.static',
              'idcops.templates',
              'idcops.migrations',
              'idcops.templatetags'],
    include_package_data=True,
    license='BSD License',
    description='A data center inventory management software',
    long_description=README,
    url='https://www.iloxp.com/',
    author='Vivian Cheung',
    author_email='wenvki@gmail.com',
    install_requires=get_requirements(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
