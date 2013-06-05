#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Administration Scripts
# Copyright (c) 2008-2012 Hive Solutions Lda.
#
# This file is part of Hive Administration Scripts.
#
# Hive Administration Scripts is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive Administration Scripts is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive Administration Scripts. If not, see <http://www.gnu.org/licenses/>.

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
import sys
import paramiko
import datetime
import cStringIO

DEBUG = False

base_dir = os.path.dirname(__file__)
base_dir = os.path.normpath(base_dir)
root_dir = os.path.join(base_dir, "..")
root_dir = os.path.normpath(root_dir)
templates_home = os.path.join(root_dir, "templates")

user_home = os.path.expanduser("~")
dropbox_base = os.path.join(user_home, "Dropbox")
dropbox_home = os.path.join(dropbox_base, "Home")
ssh_home = os.path.join(dropbox_home, "ssh")

if not user_home in sys.path: sys.path.append(user_home)
if not dropbox_base in sys.path: sys.path.append(dropbox_base)
if not dropbox_home in sys.path: sys.path.append(dropbox_home)

servers = __import__("servers")
config = servers

def get_ssh(hostname):
    username, password = servers.SERVERS_MAP.get(hostname, (None, None))
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print_host(hostname, "connecting...")
    ssh.connect(
        hostname,
        username = username,
        password = password
    )
    print_host(hostname, "connected")
    return ssh

def command(ssh, command, shell = False):
    if shell: return command_shell(ssh, command)
    else: return command_single(ssh, command)

def command_single(ssh, command):
    stdin, stdout, stderr = ssh.exec_command(command)
    data_out = stdout.readlines()
    data_err = stderr.readlines()

    stream_out = cStringIO.StringIO()
    stream_err = cStringIO.StringIO()

    for line in data_out: stream_out.write(line + "\n")
    for line in data_err: stream_err.write(line + "\n")

    stream_out.seek(0)
    stream_err.seek(0)

    if DEBUG:
        for line in data_out: print line

    for line in data_err: print line

    return stdin, stream_out, stream_err

def command_shell(ssh, command):
    channel = ssh.invoke_shell()
    stdin = channel.makefile("wb")
    stdout = channel.makefile("rb")

    stdin.write(command + "\r\n" + "exit\r\n")
    data_out = stdout.readlines()

    stream_out = cStringIO.StringIO()

    for line in data_out: stream_out.write(line + "\n")

    stream_out.seek(0)

    if DEBUG:
        for line in data_out: print line

    stdout.close()
    stdin.close()

def print_host(hostname, message):
    print "[" + hostname + "] " + message

def get_date_s():
    date_time = datetime.datetime.now()
    date_s = date_time.strftime("%Y%m%d")
    return date_s

def get_date_time_s():
    date_time = datetime.datetime.now()
    date_time_s = date_time.strftime("%Y%m%d%H%M")
    return date_time_s

cmd = command
