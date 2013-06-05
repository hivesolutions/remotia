# Remotia System

Infra-structure for the automation of common admin task that uses remote SSH sessions
to perform commands on remote machines.

## Installation

* `easy_install remotia`

## Configuration

In order to provide information for remotia configuration one must create a python
configuration file with the name `rconfig.py` and put it in one of the following
locations:

* `~`
* `~/Dropbox`
* `~/Dropbox/Home`

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
