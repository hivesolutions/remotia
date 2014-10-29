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

from . import apt
from . import common
from . import db
from . import file
from . import internal
from . import service
from . import system
from . import util

from .apt import update_apt, install_apt
from .common import config, get_ssh, command, command_single, command_shell, print_host,\
    get_date_s, get_date_time_s, cmd
from .db import mysql_dump, mysql_load, mysql_open, mysql_add_user, mysql_create_database,\
    mysql_exec
from .file import rm
from .internal import deploy_repo, deploy_colony, deploy_omni
from .service import restart_service, update_service, update_dns, update_dhcp
from .system import deploy_keys, create_users, setup_environment
from .util import uptime, reboot, get, put
