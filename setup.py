# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
    name         = 'msfi',
    version      = '1.0',
    description  = 'This module allow scripting to control the Metasploit Console',
    url          = 'http://github.com/Remigascou/msfi',
    author       = 'Remi GASCOU',
    author_email = 'remi@gascou.net',
    license      = 'GPL2',
    packages     = setuptools.find_packages(),
    classifiers  = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Topic :: Security",
    ],
    python_requires = '>=3.6',
    zip_safe     = False
)
