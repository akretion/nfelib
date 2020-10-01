#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='nfelib',
    version='0.5',
    author='Raphael Valyi',
    author_email='raphael.valyi@akretion.com',
    url='https://github.com/akretion/nfelib',
    description='nfelib: electronic invoicing library for Brazil',
    long_description=readme,
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='e-invoice NFe ERP Odoo',
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.5",
    scripts=[],
    zip_safe=False,
)
