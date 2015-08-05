#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Remotia System
# Copyright (c) 2008-2015 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2015 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import remotia.deployers as deployers

config = deployers.config

def run(method, *args):
    for hostname in config.ALL_SERVERS:
        try: method(hostname, *args)
        except BaseException as exception:
            deployers.print_host(hostname, str(exception))

def run_local(method, *args):
    for hostname in config.LOCAL_SERVERS:
        try: method(hostname, *args)
        except BaseException as exception:
            deployers.print_host(hostname, str(exception))

def run_remote(method,*args):
    for hostname in config.REMOTE_SERVERS:
        try: method(hostname, *args)
        except BaseException as exception:
            deployers.print_host(hostname, str(exception))

def run_machine(method, *args):
    for hostname in config.MACHINE_SERVERS:
        try: method(hostname, *args)
        except BaseException as exception:
            deployers.print_host(hostname, str(exception))
