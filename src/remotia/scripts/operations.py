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

import remotia.deployers as deployers

config = deployers.config

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

def service_update(hostname):
    """
    Runs a series of typical service update operation in the
    servers range for the hive infra-structure.

    These operations are safe to be run in any occasion.

    @type hostname: String
    @param hostname: The name of the host to be used for this
    operation, this should be a fully qualified name.
    """

    ssh = deployers.get_ssh(hostname)
    uptime_s = deployers.uptime(ssh)
    deployers.print_host(hostname, uptime_s)

    if hostname in config.DNS_SERVERS:
        config = config.DNS_CONFIG.get(hostname, {})
        deployers.update_dns(ssh, **config)
        deployers.print_host(hostname, "updated dns registers")

    if hostname in config.DHCP_SERVERS:
        config = config.DHCP_CONFIG.get(hostname, {})
        deployers.update_dhcp(ssh, **config)
        deployers.print_host(hostname, "updated dhcp registers")

    deployers.update_apt(ssh)
    deployers.print_host(hostname, "software upgraded")
