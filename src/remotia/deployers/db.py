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

import time

import common

def mysql_dump(ssh, database = "master", path = None, username = None, password = None):
    timestamp = int(time.time())
    path = path or "/tmp/%s_%d.sql.gz" % (database, timestamp)
    common.cmd(
        ssh,
        "mysqldump --opt --user=%s --password=%s %s | gzip > %s" %\
            (username, password, database, path)
    )
    return path

def mysql_load(ssh, database = "master", path = None, username = None, password = None):
    path_base = path.rsplit(".", 1)[0]

    common.cmd(
        ssh,
        "gzip -d %s && mysql --user=%s --password=%s %s < %s" %\
            (path, username, password, database, path_base)
    )

def mysql_open(ssh, address):
    common.cmd(
        ssh,
        "sed -i \"s/bind-address.*/bind-address=%s/g\" /etc/mysql/my.cnf" %\
            address
    )

def mysql_add_user(ssh, username, password):
    common.cmd(
        ssh,
        "mysql -e \"grant all on *.* to '%s' identified by '%s';flush privileges;\"" %\
        (username, password)
    )
    common.cmd(
        ssh,
        "mysql -e \"grant all on *.* to '%s'@'localhost' identified by '%s';flush privileges;\"" %\
        (username, password)
    )

def mysql_create_database(ssh, name, username = None, password = None):
    mysql_exec(
        ssh,
        "create schema %s default character set utf8" % name,
        username = username,
        password = password
    )

def mysql_exec(ssh, command, username = None, password = None):
    is_auth = username and password
    is_auth and common.cmd(
        ssh,
        "mysql --user=%s --password=%s -e \"%s\"" % (username, password, command)
    ) or common.cmd(
        ssh,
        "mysql -e \"%s\"" % command
    )
