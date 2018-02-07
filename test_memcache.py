from oslo_log import log as logging

import nova.conf
from nova import config
from nova import objects
from nova import context
import os
from nova import cache_utils

LOG = logging.getLogger(__name__)

CONF = nova.conf.CONF
argv = []
default_config_files = ['/etc/nova/nova.conf']
config.parse_args(argv, default_config_files=default_config_files)
objects.register_all()
context = context.get_admin_context()
os.getpid()
mc = cache_utils.get_client(CONF.consoleauth.token_ttl)
token='0d745ccf-ee97-4a26-b504-f87a39c3d060'
mc.set(token.encode('UTF-8'),'asd')
mc.get(token.encode('UTF-8'))
mc.region.backend.__dict__

