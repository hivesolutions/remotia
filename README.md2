# Remotia System

Infra-structure for the automation of common admin tasks that uses remote SSH sessions
to perform commands on remote machines.

## Installation

    pip install remotia

## Configuration

In order to provide information for remotia configuration one must create a python
configuration file with the name `rconfig.py` and put it in one of the following
locations:

* `~`
* `~/Dropbox`
* `~/Dropbox/Home`

## Usage

The basic usage of the remotia command line should follow this syntax:

    remotia ${TARGET} ${SCRIPT}

For example to run the DNS update script in the currently defined remote hosts use
the following command:

    remotia remote dns_update

You can also call direct execution methods that take the host instead of running
a script on a set of hosts for this case the syntax would be:

    remotia ${SCRIPT} ${HOST}

And an example can be the running of the backup operation of omni in a remote host,
use this method with care as it may take some time to be executed:

    remotia omni_backup ${HOST}
	
You can even add arguments to the script execution, to configure some of its behaviour
like database location username or password, a simple DBMS setup could be done using:

    remotia mysql_deploy ${HOST} ${USERNAME} ${PASSWORD}

### Example

	#!/usr/bin/python
	# -*- coding: utf-8 -*-
	
	SERVERS = (
	    ("remote1.host.com", "root", "root"),
	    ("remote2.host.com", "root", "root"),
	    ("local1.host.com", "root", "root"),
	    ("local2.host.com", "root", "root"),
	    ("machine1.host.com", "root", "root")
	)
	
	SERVERS_MAP = {}
	
	ALL_SERVERS = ()
	
	REMOTE_SERVERS = (
	    "remote1.host.com",
	    "remote2.host.com"
	)
	
	LOCAL_SERVERS = (
	    "local1.host.com",
	    "local2.host.com"
	)
	
	MACHINE_SERVERS = (
	    "machine1.host.com",
	)
	
	ALL_SERVERS = SERVERS_MAP.keys()