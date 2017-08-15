# -*- coding: utf-8 -*-

import nova.conf
from nova import config
from nova import utils

utils.period_heartbeat_file.func_defaults
CONF = nova.conf.CONF
argv = []
default_config_files = ['/etc/ironic-nova-compute/ironic-nova-compute.conf']
config.parse_args(argv, default_config_files=default_config_files)
utils.period_heartbeat_file.func_defaults
CONF.heartbeat_interval

CONF.set_default('heartbeat_interval',5)
