from oslo_log import log as logging

import nova.conf
from nova import config
from nova import objects
from nova import context
from nova import db
from nova.db.sqlalchemy import models

LOG = logging.getLogger(__name__)

CONF = nova.conf.CONF
argv = []
default_config_files = ['/etc/nova/nova.conf']
config.parse_args(argv, default_config_files=default_config_files)
objects.register_all()
context = context.get_admin_context()
nodes = objects.ComputeNodeList.get_all(context)
[it['deleted'] for it in nodes]

import nova.db.sqlalchemy.api as api
cxt = api.get_context_manager(context)
t=cxt.writer.using(context)
s=t.__enter__()
s.query(models.ComputeNode).first()
s.rollback()
s.close()


cn = objects.ComputeNode(context)
cn.memory_mb_used

