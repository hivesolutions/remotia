#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Remotia System
# Copyright (C) 2008-2014 Hive Solutions Lda.
#
# This file is part of Hive Remotia System.
#
# Hive Remotia System is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Remotia System is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Remotia System. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2014 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import os
import glob
import setuptools

setuptools.setup(
    name = "remotia",
    version = "0.2.0",
    author = "Hive Solutions Lda.",
    author_email = "development@hive.pt",
    description = "Remotia System",
    license = "GNU General Public License (GPL), Version 3",
    keywords = "remotia ssh automation console",
    url = "http://remotia.hive.pt",
    zip_safe = False,
    packages = [
        "remotia",
        "remotia.base",
        "remotia.deployers",
        "remotia.scripts"
    ],
    package_dir = {
        "" : os.path.normpath("src")
    },
    package_data = {
        "remotia" : ["templates/*"]
    },
    install_requires = [
        "legacy",
        "paramiko"
    ],
    entry_points = {
        "console_scripts" : [
            "remotia = remotia.base.run:main"
        ]
    },
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4"
    ]
)
