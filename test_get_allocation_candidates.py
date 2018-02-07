from oslo_log import log as logging
from oslo_utils import importutils
import nova.conf
from nova import config
from nova import objects
from nova import context
from nova.scheduler import utils
from nova.scheduler import client as scheduler_client

CONF = nova.conf.CONF

logging.setup(CONF, 'nova')
LOG = logging.getLogger(__name__)

argv = []
default_config_files = ['/etc/nova/nova.conf']
config.parse_args(argv, default_config_files=default_config_files)
objects.register_all()
context = context.get_admin_context()

client = scheduler_client.SchedulerClient()
placement_client = client.reportclient

instance_uuid='fdc43c5c-49e1-448b-8cb1-c0d73030697f'
request_spec = objects.RequestSpec.get_by_instance_uuid(context, instance_uuid)
resources = utils.resources_from_request_spec(request_spec)
res=placement_client.get_allocation_candidates(resources)
alloc_reqs, provider_summaries = res