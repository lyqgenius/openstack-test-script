import rados
import rbd
import imp
rbd = imp.load_source('rbd', '/usr/lib/python2.7/site-packages/rbd.py')

image_name = 'volume-a4f4daca-2b35-45a5-9e45-a145452050b1'

client = rados.Rados(
    rados_id='cinder',
    clustername='ceph',
    conffile='/etc/ceph/ceph.conf')
pool = 'volumes'
client.connect(timeout=60)
ioctx = client.open_ioctx(pool)
rbd_image = rbd.Image(ioctx, image_name)
rbd_image.list_snaps()
rbd_image.close()
ioctx.close()
client.shutdown()

client1 = rados.Rados(
    rados_id='cinder',
    clustername='ceph',
    conffile='/etc/ceph/ceph.conf')
client1.connect(timeout=60)
ioctx1 = client1.open_ioctx(pool)
rbd_image1 = rbd.Image(ioctx1, image_name)
rbd_image1.list_snaps()
rbd_image1.close()
ioctx1.close()
client1.shutdown()

client2 = rados.Rados(
    rados_id='cinder',
    clustername='ceph',
    conffile='/etc/ceph/ceph.conf')
client2.connect(timeout=60)
ioctx2 = client1.open_ioctx(pool)
rbd_image2 = rbd.Image(ioctx2, image_name)
rbd_image2.list_snaps()
rbd_image2.close()
ioctx2.close()
client2.shutdown()




