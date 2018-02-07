from nova.virt.libvirt import config as vconfig
from lxml import etree

lease_config = vconfig.LibvirtConfigGuestLease(key_value='uuid', target_path='uuid')
lease_config.to_xml()

str=lease_config.to_xml()
xml_doc = etree.fromstring(str)
lease_config.parse_dom(xml_doc)



