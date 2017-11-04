#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='nfelib',
    version='0.1',
    author='Raphael Valyi',
    author_email='raphael.valyi@akretion.com',
    url='https://github.com/akretion/nfelib',
    description='nfelib: electronic invoicing library for Brazil',
    long_description=open('README.rst').read(),
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        "Operating System :: OS Independent",
    ],
    keywords='e-invoice NFe ERP Odoo',
    packages=find_packages(),
    include_package_data=True,
    install_requires={
        'futures; python_version == "2.7"'
    },
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    scripts=[],
    zip_safe=False,
)
