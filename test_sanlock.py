#!/usr/bin/python
import sys,os
import time
from multiprocessing import Process
import tempfile
import sanlock

RESOURCE_NAME = "8e38c2837de14cbe83f578153d8dd808"
LOCKSPACE_NAME = '__LIBVIRT__DISKS__'
SANLOCK_PATH = '/var/lib/libvirt/sanlock/'
SANLOCK_PATH = os.path.abspath(SANLOCK_PATH+RESOURCE_NAME)
offset = sanlock.get_alignment(SANLOCK_PATH)
SNLK_DISKS = [(SANLOCK_PATH,offset)]


def sanlock_acquire(hostId, lockspacePath, leasePath):
    sfd = sanlock.register()
    if not sanlock.inq_lockspace(LOCKSPACE_NAME, hostId,
                                 lockspacePath):
        msg = "Try to acquire host id %s:%s:%s:0" % (LOCKSPACE_NAME, hostId, lockspacePath)
        print(msg)
        sanlock.add_lockspace(LOCKSPACE_NAME, hostId, lockspacePath)
    msg = "Try to acquire leader lease:%s" % str(leasePath)
    print(msg)
    sanlock.acquire(LOCKSPACE_NAME, RESOURCE_NAME, [(leasePath, 0)], sfd)

if __name__ == "__main__":
    host_id = int(sys.argv[1])
    lockspace_path = sys.argv[2]
    lease_path = sys.argv[3]
    hosts_list = sanlock.get_hosts(LOCKSPACE_NAME)
    msg = 'sanlock hosts:%s' % str(hosts_list)
    print msg
    sanlock_acquire(host_id,lockspace_path,lease_path)
    time.sleep(180)
    resource_owners = sanlock.read_resource_owners(
                LOCKSPACE_NAME, RESOURCE_NAME, SNLK_DISKS)
    print 'resource_owners:%s' % str(resource_owners)
