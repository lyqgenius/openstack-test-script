import sys
import pdb
import chardet

from oslo_log import log as logging

import nova.conf
from nova import config
from nova import objects
from nova import context
from nova.scheduler import rpcapi as scheduler_rpcapi
from nova.scheduler import utils as scheduler_utils
from nova import utils as nova_utils

CONF = nova.conf.CONF
argv = []
default_config_files = ['/etc/nova/nova.conf']
config.parse_args(argv, default_config_files=default_config_files)
objects.register_all()
context = context.get_admin_context()
inst = objects.Instance.get_by_uuid(context,'a62179e2-d00d-4a68-bd85-b0ff54e3c178')
filter_properties = {'ignore_hosts': [],'rs_aggregate_id': 3}
system_metadata = nova_utils.instance_sys_meta(inst)
image = nova_utils.get_image_from_system_metadata(system_metadata)
request_spec = scheduler_utils.build_request_spec(context,image,[inst])
spec_obj = objects.RequestSpec.from_primitives(context,request_spec, filter_properties)
scheduler_rpcapi = scheduler_rpcapi.SchedulerAPI()
destinations = scheduler_rpcapi.select_destinations(context, spec_obj)
print destinations
