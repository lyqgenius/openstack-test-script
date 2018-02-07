from oslo_log import log as logging
from oslo_utils import importutils
import nova.conf
from nova import config
from nova import objects
from nova import context

CONF = nova.conf.CONF

logging.setup(CONF, 'nova')
LOG = logging.getLogger(__name__)

argv = []
default_config_files = ['/etc/nova/nova.conf']
config.parse_args(argv, default_config_files=default_config_files)
objects.register_all()
context = context.get_admin_context()

rp_uuid='51533989-1a99-41aa-b0e7-1e901e2bd5f3'
rp_name='CUSTOM_BARE_DESK_HOST'
inv_data={'CUSTOM_BARE_DESK': {'total': 3,'min_unit': 1,'max_unit': 3,'step_size': 1,}}
report_client_class = importutils.import_class('nova.scheduler.client.report.SchedulerReportClient')
reportclient = report_client_class()
reportclient.set_inventory_for_provider(rp_uuid,rp_name,inv_data)

resources = {}
resources["CUSTOM_BARE_DESK"]=1
res = reportclient.get_allocation_candidates(resources)

alloc_request=res[0][0]
consumer_uuid='118ba92b-8686-41de-99cb-8bb5683d42bf'
project_id="a2794be2207a45b5be5b2423bfa08c2c"
user_id='15b1ac50c8764fc0bbd06de08ba64c95'
res_claim_resources=reportclient.claim_resources(consumer_uuid,alloc_request,project_id,user_id)

class Instance():pass

instance = Instance()
setattr(instance,'uuid',consumer_uuid)
res_get_allocations = reportclient.get_allocations_for_instance(rp_uuid,instance)