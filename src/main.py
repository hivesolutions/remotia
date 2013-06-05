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

import scripts
import deployers

def start_machine(hostname):
    ssh = deployers.get_ssh(hostname)
    deployers.deploy_keys(ssh)
    deployers.setup_environment(
        ssh,
        hostname = "tobias.hive",
        ip_address = "172.16.0.125",
        netmask = "255.255.0.0",
        broadcast = "172.16.255.255",
        network = "172.16.0.0",
        gateway = "172.16.0.26",
        domain = "hive",
        dns_server_1 = "172.16.0.11",
        dns_server_2 = "172.16.0.12"
    )

if __name__ == "__main__":
    pass
    #start_machine("172.16.0.125")
    #scripts.run_machine(scripts.upgrade)
    #scripts.omni_backup("node2.startomni.com")
    #scripts.cleermob_backup("servidor5.hive")
