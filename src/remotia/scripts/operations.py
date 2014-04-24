#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Remotia System
# Copyright (c) 2008-2014 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2014 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import remotia.deployers as deployers

config = deployers.config

def init(hostname):
    """
    Initializes the system, creating a series of files that
    may be required for a series of base operations.

    This script is recommended for every setup of a machine
    running under the current infrastructure.

    @type hostname: String
    @param hostname: The name of the host to be used for this
    operation, this should be a fully qualified name.
    """

    ssh = deployers.get_ssh(hostname)
    deployers.print_host(hostname, "deploying the ssh keys...")
    deployers.deploy_keys(ssh)
    deployers.print_host(hostname, "finished deploying the ssh keys")
    deployers.print_host(hostname, "creating users")
    deployers.create_users(ssh, config.USERS)
    deployers.print_host(hostname, "finished creating users...")

def reboot(hostname):
    ssh = deployers.get_ssh(hostname)
    deployers.reboot(ssh)
    deployers.print_host(hostname, "reboot order sent")

def upgrade(hostname):
    ssh = deployers.get_ssh(hostname)
    deployers.print_host(hostname, "system upgrading...")
    deployers.update_apt(ssh)
    deployers.print_host(hostname, "system upgraded")
    deployers.reboot(ssh)
    deployers.print_host(hostname, "reboot order sent")

def dns_update(hostname):
    ssh = deployers.get_ssh(hostname)
    if not hostname in config.DNS_SERVERS: return
    config_v = config.DNS_CONFIG.get(hostname, {})
    deployers.update_dns(ssh, **config_v)
    deployers.print_host(hostname, "updated dns registers")

def dhcp_update(hostname):
    ssh = deployers.get_ssh(hostname)
    if not hostname in config.DHCP_SERVERS: return
    config_v = config.DHCP_CONFIG.get(hostname, {})
    deployers.update_dhcp(ssh, **config_v)
    deployers.print_host(hostname, "updated dhcp registers")

def apt_update(hostname):
    ssh = deployers.get_ssh(hostname)
    deployers.print_host(hostname, "upgrading software...")
    deployers.update_apt(ssh)
    deployers.print_host(hostname, "software upgraded")

def service_update(hostname):
    """
    Runs a series of typical service update operations in the
    range of servers for the hive infra-structure.

    These operations are safe to be run in any occasion as they
    do not create any data destruction or change.

    @type hostname: String
    @param hostname: The name of the host to be used for this
    operation, this should be a fully qualified name.
    """

    ssh = deployers.get_ssh(hostname)
    uptime_s = deployers.uptime(ssh)
    deployers.print_host(hostname, uptime_s)

    dns_update(hostname)
    dhcp_update(hostname)
    apt_update(hostname)
