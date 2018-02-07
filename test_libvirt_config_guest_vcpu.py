from nova.virt.libvirt import config as vconfig

guest = vconfig.LibvirtConfigGuest()
guest.vcpus = 4
print guest.to_xml()