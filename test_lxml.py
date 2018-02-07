from lxml import etree

address = etree.Element("address",
                        domain='domain',
                        bus='bus',
                        slot='slot',
                        function='function')
source = etree.Element("source")
source.append(address)
xml_str = etree.tostring(source, pretty_print=True)


lockspace_name='__LIBVIRT__DISKS__'
lockspace = etree.Element('lockspace',lockspace_name)
lockspace.append(lockspace_name)
etree.tostring(lockspace, pretty_print=True)
