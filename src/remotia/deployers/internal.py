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

from remotia.deployers import apt
from remotia.deployers import common

def deploy_repo(ssh, path = "/opt/repo.extra"):
    common.cmd(ssh, "mkdir -p " + path)
    common.cmd(ssh, "cd " + path + "; wget https://raw.github.com/hivesolutions/bootstrap/master/lib/bootstrap.py")
    common.cmd(ssh, "cd " + path + "; python bootstrap.py --download", shell = True)
    common.cmd(ssh, "cd " + path + "; python bootstrap.py --bootstrap", shell = True)

def deploy_colony(ssh, path = "/opt/repo.extra"):
    deploy_repo(ssh, path = path)

def deploy_omni(ssh, path = "/opt/repo.extra"):
    apt.install_apt(ssh, "python-mysqldb")
    apt.install_apt(ssh, "python-imaging")
    apt.install_apt(ssh, "python-reportlab")
    apt.install_apt(ssh, "python-crypto")
    apt.install_apt(ssh, "python-tz")
    deploy_repo(ssh, path = path)
