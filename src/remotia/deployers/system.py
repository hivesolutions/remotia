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
import jinja2
import tempfile

import common

def deploy_keys(ssh):
    private_key = os.path.join(common.dropbox_home, "ssh", "id_rsa")
    public_key = os.path.join(common.dropbox_home, "ssh", "id_rsa.pub")
    known_hosts = os.path.join(common.dropbox_home, "ssh", "known_hosts")
    authorized_keys = os.path.join(common.dropbox_home, "ssh", "authorized_keys")

    ftp = ssh.open_sftp()
    try:
        try: ftp.mkdir("/root/.ssh", 0700)
        except: pass
        ftp.put(private_key, "/root/.ssh/id_rsa")
        ftp.put(public_key, "/root/.ssh/id_rsa.pub")
        ftp.put(known_hosts, "/root/.ssh/known_hosts")
        ftp.put(authorized_keys, "/root/.ssh/authorized_keys")
        ftp.chmod("/root/.ssh/id_rsa", 0600)
        ftp.chmod("/root/.ssh/id_rsa.pub", 0644)
        ftp.chmod("/root/.ssh/known_hosts", 0644)
        ftp.chmod("/root/.ssh/authorized_keys", 0600)
    finally:
        ftp.close()

def create_users(ssh, users):
    for username, password in users:
        common.cmd(ssh, "useradd " + username)
        common.cmd(ssh, "echo \"" + username + "\":" + password + " | chpasswd")

def setup_environment(ssh, **kwargs):
    hostname = kwargs.get("hostname", "localhost")
    ip_address = kwargs.get("ip_address", None)
    netmask = kwargs.get("netmask", None)
    broadcast = kwargs.get("broadcast", None)
    network = kwargs.get("network", None)
    gateway = kwargs.get("gateway", None)
    domain = kwargs.get("domain", None)
    dns_server_1 = kwargs.get("dns_server_1", None)
    dns_server_2 = kwargs.get("dns_server_2", None)

    if not ip_address: return
    if not netmask: return
    if not broadcast: return
    if not network: return
    if not gateway: return
    if not domain: return
    if not dns_server_1: return
    if not dns_server_2: return

    net = dict(
        hostname = hostname,
        ip_address = ip_address,
        netmask = netmask,
        broadcast = broadcast,
        network = network,
        gateway = gateway,
        domain = domain,
        dns_servers = [dns_server_1, dns_server_2]
    )

    dir_path = tempfile.mkdtemp()

    loader = jinja2.FileSystemLoader(common.templates_home)
    env = jinja2.Environment(loader = loader)
    template = env.get_template("hostname.tpl")
    data = template.render(net = net)
    file = open(dir_path + "/hostname", "wb")
    try: file.write(data)
    finally: file.close()

    template = env.get_template("interfaces.tpl")
    data =  template.render(net = net)
    file = open(dir_path + "/interfaces", "wb")
    try: file.write(data)
    finally: file.close()

    template = env.get_template("resolv.conf.tpl")
    data = template.render(net = net)
    file = open(dir_path + "/resolv.conf", "wb")
    try: file.write(data)
    finally: file.close()

    ftp = ssh.open_sftp()
    try:
        ftp.put(dir_path + "/hostname", "/etc/hostname")
        ftp.put(dir_path + "/resolv.conf", "/etc/resolv.conf")
        ftp.put(dir_path + "/interfaces", "/etc/network/interfaces")
    finally:
        ftp.close()
