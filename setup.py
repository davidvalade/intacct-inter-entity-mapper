#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    author="David Valade",
    author_email='david@valadeservices.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A helper to assist with the GL account mappings required by Sage Intacct to track Due-to and Due-from transactions.",
    entry_points={
        'console_scripts': [
            'intacct_inter_entity_account_mapping_helper=intacct_inter_entity_account_mapping_helper.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='intacct_inter_entity_account_mapping_helper',
    name='intacct_inter_entity_account_mapping_helper',
    packages=find_packages(include=['intacct_inter_entity_account_mapping_helper', 'intacct_inter_entity_account_mapping_helper.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/davidvalade/intacct_inter_entity_account_mapping_helper',
    version='0.1.0',
    zip_safe=False,
)
