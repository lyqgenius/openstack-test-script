from oslo_log import log as logging
import nova.conf
from nova import config
from os_brick.initiator import connector
from oslo_utils import importutils
from os_brick.initiator import linuxfc
from nova import utils
import nova.netconf
import nova.virt.libvirt.driver
from nova import objects

# import shlex
# from oslo_privsep import priv_context
# priv_context.init(root_helper=shlex.split(utils.get_root_helper()))



CONF = nova.conf.CONF
argv = []
default_config_files = ['/etc/nova/nova.conf']
config.parse_args(argv, default_config_files=default_config_files)
CONF.import_opt('compute_topic', 'nova.compute.rpcapi')
logging.setup(CONF, 'nova')
LOG = logging.getLogger('nova.compute')
utils.monkey_patch()
objects.register_all()

root_helper = utils.get_root_helper()
root_helper = 'sudo privsep-helper --config-file /etc/nova/nova.conf --config-dir /etc/nova'
connector.get_connector_properties(root_helper, CONF.my_block_storage_ip,CONF.libvirt.iscsi_use_multipath,enforce_multipath=True,host=CONF.host)


connector = importutils.import_class('os_brick.initiator.connector.FibreChannelConnector')
connector.get_connector_properties(root_helper,host='i620d7-app',multipath=False,enforce_multipath=True,execute=None)

fc = linuxfc.LinuxFibreChannel(root_helper,execute=None)

