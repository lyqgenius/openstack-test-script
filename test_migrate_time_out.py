from oslo_log import log as logging

import nova.conf
from nova import config
from nova import objects
from nova import context
from oslo_utils import timeutils

LOG = logging.getLogger(__name__)

CONF = nova.conf.CONF
argv = []
default_config_files = ['/etc/nova/nova.conf']
config.parse_args(argv, default_config_files=default_config_files)
objects.register_all()
context = context.get_admin_context()
migrate_time_out = 1800
uuid = 'f119bcda-c6e4-49d2-8ce4-5a18af40ede0'
instance = objects.Instance.get_by_uuid(context,uuid)

updated_at = instance.updated_at
timeutils.is_older_than(updated_at, migrate_time_out)

