#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click',]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Hobnobpirate",
    author_email='hobnobpirate@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Package to examine parts of the Mach-O file. Purely academic and not for operational use at this time.",
    entry_points={
        'console_scripts': [
            'mach-o-peek=mach_o_peek.cli:cli',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='mach_o_peek',
    name='mach_o_peek',
    packages=find_packages(include=['mach_o_peek']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/hobnobpirate/mach_o_peek',
    version='0.1.0',
    zip_safe=False,
)
