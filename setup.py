#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0',
                'requests==2.22.0',
                'jsonschema==3.0.2',
                'jsonschema[format]',
                'validators==0.13.0',
                'tabulate==0.8.3',
                'pyyaml==5.1.2']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest']

setup(
    classifiers=[
        'Development Status :: 3 - Release Candidate',
        'Intended Audience :: Developers/Penetration Testers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Environment :: Console',
        'Topic :: Security'
    ],
    description="DrHEADer helps with the audit of security headers received in response to a single request or a list of requests.",
    entry_points={
        'console_scripts': [
            'drheader=drheader.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='drheader',
    author='Santander UK Security Engineering',
    name='drheader',
    packages=['drheader'],
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/santandersecurityresearch/drheader',
    version='1.1.0',
    zip_safe=False,
)
