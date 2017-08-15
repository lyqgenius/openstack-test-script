# -*- coding: utf-8 -*-

import sys
import pdb
import chardet

from oslo_log import log as logging

import nova.conf
from nova import config
from nova import objects
from nova import context

LOG = logging.getLogger(__name__)

CONF = nova.conf.CONF
argv = []
default_config_files = ['/etc/nova/nova.conf']
config.parse_args(argv, default_config_files=default_config_files)
objects.register_all()
context = context.get_admin_context()