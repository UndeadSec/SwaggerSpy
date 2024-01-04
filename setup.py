#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup
from os import path
import io

pwd = path.abspath(path.dirname(__file__))
with io.open(path.join(pwd, "README.md"), encoding="utf-8") as readme:
    desc = readme.read()

setup(
    name='swaggerspy',
    version='1.0.0',
    packages=['swaggerspy'],
    long_description=desc,
    long_description_content_type="text/markdown",
    install_requires=[
        'requests',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'swaggerspy = swaggerspy.__main__:main',
        ],
    },
    author='Alisson Moretto (UndeadSec)',
    description='SwaggerSpy is a tool designed for automated Open Source Intelligence (OSINT) on SwaggerHub.',
    url='https://github.com/UndeadSec/SwaggerSpy',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    keywords=["python", "pentest", "secret", "bugbounty", "security"],
)
