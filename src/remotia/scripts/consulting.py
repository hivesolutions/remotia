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

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import os

import remotia.deployers as deployers

config = deployers.config

def cleermob_backup(hostname):
    date_s = deployers.get_date_s()
    file_name = "cleermob_%s.sql.gz" % date_s
    cleermob_path = os.path.join(config.BACKUPS_PATH, "cleermob")
    local_path = os.path.join(cleermob_path, file_name)
    if not os.path.exists(cleermob_path): os.makedirs(cleermob_path)

    ssh = deployers.get_ssh(hostname)
    deployers.print_host(hostname, "dumping database...")
    remote_path = deployers.mysql_dump(
        ssh,
        database = config.CLEER_DB_NAME,
        username = config.CLEER_DB_USERNAME,
        password = config.CLEER_DB_PASSWORD
    )
    deployers.print_host(hostname, "dumped database")
    deployers.print_host(hostname, "transferring file...")
    deployers.get(ssh, remote_path, local_path, remove = True)
    deployers.print_host(hostname, "file transfered")
