from oslo_log import log as logging
import hastack.has.conf as ha_conf
from nova import config
from nova import objects
import hastack.openstack.openstack_utils as openstack_utils
from hastack.openstack.openstack_api.api import ComputeAPI
from nova.objects import instance as instance_obj

LOG = logging.getLogger(__name__)
CONF = ha_conf.CONF
argv = []
default_config_files = ['/etc/nova/nova.conf']
config.parse_args(argv, default_config_files=default_config_files)
objects.register_all()
ctxt = openstack_utils.create_context()
INSTANCE_DEFAULT_FIELDS = instance_obj.INSTANCE_DEFAULT_FIELDS

inst_id = '8c9f2873-cf42-4df0-99c0-c7ac41fa3313'
host = 'test-compute2'
compute_api = ComputeAPI()
inst = compute_api.get_instance_by_uuid(ctxt, inst_id,
                                        expected_attrs=INSTANCE_DEFAULT_FIELDS)
compute_api.evacuate(ctxt.elevated(), inst, host, True)

from nova import compute
compute_api = compute.API()
compute_api.evacuate(ctxt.elevated(), inst, host, True,force=False)
