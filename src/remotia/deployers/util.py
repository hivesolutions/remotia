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

import common

def uptime(ssh):
    _stdin, stdout, _stderr = common.cmd(ssh, "uptime")
    data = stdout.read()
    data = data.strip()
    up, _users, _load = data.split(",", 2)
    _time, up, up_value, up_unit = up.split(" ")
    return up_value + " " + up_unit

def reboot(ssh):
    common.cmd(ssh, "reboot")

def get(ssh, remote_path, local_path, remove = False):
    ftp = ssh.open_sftp()
    try:
        ftp.get(remote_path, local_path)
        if remove: ftp.remove(remote_path)
    finally:
        ftp.close()

def put(ssh, local_path, remote_path, remove = False):
    ftp = ssh.open_sftp()
    try:
        ftp.put(local_path, remote_path)
        if remove: ftp.remove(local_path)
    finally:
        ftp.close()
