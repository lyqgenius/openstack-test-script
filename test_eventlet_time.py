import time, os
from threading import Thread
import eventlet

eventlet.monkey_patch(os=False)
import drsstack.rs.conf
from oslo_log import log as logging
from oslo_utils import timeutils

LOG = logging.getLogger(__name__)
import drsstack.openstack.openstack_utils as openstack_utils

CONF = drsstack.rs.conf.CONF
argv = []
default_config_files = ['/etc/nova/nova.conf']
CONF(argv, default_config_files=default_config_files)

heartbeat_file = 'test.heartbeat'
heartbeat_interval = CONF.heartbeat_interval_rs


def heartbeat_process():
    while True:
        # create a file in specific directory
        strtime = timeutils.strtime()
        file_path = CONF.heartbeat_file_path + "/%s" % heartbeat_file + strtime
        try:
            if not os.path.exists(CONF.heartbeat_file_path):
                openstack_utils.execute('mkdir', '-p', "%s" %
                                        CONF.heartbeat_file_path,
                                        run_as_root=True)
            if not os.path.isfile(file_path):
                openstack_utils.execute("touch", file_path,
                                        run_as_root=True)
            time.sleep(heartbeat_interval)
        except Exception as ex:
            # catch all the exception avoiding threading exits
            LOG.error("Write to file failed %s", ex)
            time.sleep(heartbeat_interval)


heartbeat_thread = Thread(target=heartbeat_process)
heartbeat_thread.setDaemon(True)
heartbeat_thread.start()

eventlet.getcurrent().wait()

timeutils.strtime();time.sleep(heartbeat_interval);timeutils.strtime()
