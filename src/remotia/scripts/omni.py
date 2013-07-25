#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Remotia System
# Copyright (c) 2008-2012 Hive Solutions Lda.
#
# This file is part of Hive Remotia System.
#
# Hive Remotia System is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive Remotia System is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive Remotia System. If not, see <http://www.gnu.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2012 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import os

import db
import remotia.deployers as deployers

config = deployers.config

def omni_deploy(hostname, local_path = None):
    ssh = deployers.get_ssh(hostname)
    deployers.print_host(hostname, "deploying mysql...")
    db.mysql_deploy(hostname)
    deployers.print_host(hostname, "deployed mysql")
    deployers.print_host(hostname, "setting users...")
    deployers.mysql_add_user(ssh, config.OMNI_DB_USERNAME, config.OMNI_DB_PASSWORD)
    deployers.print_host(hostname, "transferring file...")
    deployers.put(ssh, local_path, "/tmp/omni_deploy.tar.gz", remove = False)
    deployers.print_host(hostname, "creating database...")
    deployers.mysql_create_database(
        ssh,
        config.OMNI_DB_NAME,
        username = config.OMNI_DB_USERNAME,
        password = config.OMNI_DB_PASSWORD
    )
    deployers.print_host(hostname, "created database")
    deployers.print_host(hostname, "loading database...")
    deployers.mysql_load(
        ssh,
        database = config.OMNI_DB_NAME,
        path = "/tmp/omni_deploy.tar.gz",
        username = config.OMNI_DB_USERNAME,
        password = config.OMNI_DB_PASSWORD
    )
    deployers.print_host(hostname, "loaded database")
    deployers.print_host(hostname, "removing temporary files...")
    deployers.rm(ssh, "/tmp/omni_deploy.tar")
    deployers.rm(ssh, "/tmp/omni_deploy.tar.gz")
    deployers.print_host(hostname, "removed temporary files")

def omni_backup(hostname):
    date_s = deployers.get_date_s()
    file_name = "omni_%s.sql.gz" % date_s
    omni_path = os.path.join(config.BACKUPS_PATH, "omni")
    local_path = os.path.join(omni_path, file_name)
    if not os.path.exists(omni_path): os.makedirs(omni_path)

    ssh = deployers.get_ssh(hostname)
    deployers.print_host(hostname, "dumping database...")
    remote_path = deployers.mysql_dump(
        ssh,
        database = config.OMNI_DB_NAME,
        username = config.OMNI_DB_USERNAME,
        password = config.OMNI_DB_PASSWORD
    )
    deployers.print_host(hostname, "dumped database")
    deployers.print_host(hostname, "transferring file...")
    deployers.get(ssh, remote_path, local_path, remove = True)
    deployers.print_host(hostname, "file transfered, stored in '%s'" % local_path)
