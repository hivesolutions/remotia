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

import sys

import remotia

def main():
    # validates that the provided number of arguments
    # is the expected one, in case it's not raises a
    # runtime error indicating the problem
    if len(sys.argv) < 3: raise RuntimeError("Invalid number of arguments")

    # unpacks the second and third command line arguments
    # as the scope of the execution and the name of the
    # script to be executed
    scope = sys.argv[1]
    script_name = sys.argv[2]

    # retrieves the set of extra arguments to be sent to the
    # command to be executed, (this may be dangerous)
    args =  sys.argv[3:]

    # retrieves both the loader command for the current
    # scope and the script to be executed and then used
    # them to run the requested command
    is_command = hasattr(remotia, "run_" + scope)
    if is_command: command = getattr(remotia, "run_" + scope)
    else: command = getattr(remotia, scope)
    is_script = hasattr(remotia, script_name)
    if is_script: script = getattr(remotia, script_name)
    else: script = script_name
    command(script, *args)

if __name__ == "__main__":
    main()
