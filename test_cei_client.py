from oslo_log import log as logging

import nova.conf
import datetime
from oslo_utils import timeutils
import drsstack.rs.conf
import drsstack.openstack.openstack_utils as openstack_utils
from gnocchiclient import client as gnocchi_client

CONF = drsstack.rs.conf.CONF
argv = []
default_config_files = ['/etc/nova/nova.conf']
CONF(argv, default_config_files=default_config_files)
group_name = drsstack.rs.conf.client.CLIENT_GROUP_NAME
auth_plugin = openstack_utils.create_auth_plugin(CONF, group_name)
kwargs = {'auth': auth_plugin}
session = openstack_utils.create_client_session(CONF, group_name, **kwargs)
args = {'session': session,}
gclient = gnocchi_client.Client('1', **args)
resource_id='51533989-1a99-41aa-b0e7-1e901e2bd5f3'
start_time = timeutils.parse_isotime(timeutils.strtime())
start_time = start_time.replace(tzinfo=None)
interval = 60
query_start = start_time - datetime.timedelta(minutes=interval)
metrics = gclient.metric.get_measures('cpu_util',resource_id=resource_id,start=query_start)
isinstance(metrics[0], (list, tuple, set, frozenset))