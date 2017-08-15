import datetime
from oslo_utils import timeutils
import drsstack.rs.conf
import drsstack.openstack.openstack_client as openstack_client

CONF = drsstack.rs.conf.CONF
argv = []
default_config_files = ['/etc/nova/nova.conf']
CONF(argv, default_config_files=default_config_files)

resource_id='38df37a9-5d8d-46f0-b75d-0d327edac0b1'
meter='memory.usage'
start_time = timeutils.parse_isotime(timeutils.strtime())
start_time = start_time.replace(tzinfo=None)
interval = CONF.rs_instance_cpu_ut_interval
query_start = start_time - datetime.timedelta(minutes=interval)
gnocchi_client = openstack_client.get_gnocchi_client()
metric = gnocchi_client.metric
metrics = metric.get_measures(meter,resource_id=resource_id,start=query_start)
print metrics
