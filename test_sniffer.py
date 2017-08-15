#!/usr/bin/env python
# coding=utf-8
import ctypes
import os
import socket
import struct


class IP(ctypes.Structure):
    _fields_ = [
        ("ihl", ctypes.c_ubyte, 4),
        ("version", ctypes.c_ubyte, 4),
        ("tos", ctypes.c_ubyte),
        ("len", ctypes.c_ushort),
        ("id", ctypes.c_ushort),
        ("offset", ctypes.c_ubyte),
        ("ttl", ctypes.c_ubyte),
        ("protocol_num", ctypes.c_ubyte),
        ("sum", ctypes.c_ushort),
        ("src", ctypes.c_ulong),
        ("dst", ctypes.c_ulong)
    ]

    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):
        self.protocol_map = {0: "HOPOPT         ",
                             1: "ICMP           ",
                             2: "IGMP           ",
                             3: "GGP            ",
                             4: "IP             ",
                             5: "ST             ",
                             6: "TCP            ",
                             7: "CBT            ",
                             8: "EGP            ",
                             9: "IGP            ",
                             10: "BBN-RCC-MON    ",
                             11: "NVP-II         ",
                             12: "PUP            ",
                             13: "ARGUS          ",
                             14: "EMCON          ",
                             15: "XNET           ",
                             16: "CHAOS          ",
                             17: "UDP            ",
                             18: "MUX            ",
                             19: "DCN-MEAS       ",
                             20: "HMP            ",
                             21: "PRM            ",
                             22: "XNS-IDP        ",
                             23: "TRUNK-1        ",
                             24: "TRUNK-2        ",
                             25: "LEAF-1         ",
                             26: "LEAF-2         ",
                             27: "RDP            ",
                             28: "IRTP           ",
                             29: "ISO-TP4        ",
                             30: "NETBLT         ",
                             31: "MFE-NSP        ",
                             32: "MERIT-INP      ",
                             33: "DCCP           ",
                             34: "3PC            ",
                             35: "IDPR           ",
                             36: "XTP            ",
                             37: "DDP            ",
                             38: "IDPR-CMTP      ",
                             39: "TP++           ",
                             40: "IL             ",
                             41: "IPv6           ",
                             42: "SDRP           ",
                             43: "IPv6-Route     ",
                             44: "IPv6-Frag      ",
                             45: "IDRP           ",
                             46: "RSVP           ",
                             47: "GRE            ",
                             48: "DSR            ",
                             49: "BNA            ",
                             50: "ESP            ",
                             51: "AH             ",
                             52: "I-NLSP         ",
                             53: "SWIPE          ",
                             54: "NARP           ",
                             55: "MOBILE         ",
                             56: "TLSP           ",
                             57: "SKIP           ",
                             58: "IPv6-ICMP      ",
                             59: "IPv6-NoNxt     ",
                             60: "IPv6-Opts      ",
                             62: "CFTP",
                             63: "IANA",
                             64: "SHB",
                             65: "KRYPTOLAN      ",
                             66: "RVD            ",
                             67: "IPPC           ",
                             69: "SAT-MON        ",
                             70: "VISA           ",
                             71: "IPCV           ",
                             72: "CPNX           ",
                             73: "CPHB           ",
                             74: "WSN            ",
                             75: "PVP            ",
                             76: "BR-SAT-MON     ",
                             77: "SUN-ND         ",
                             78: "WB-MON         ",
                             79: "WB-EXPAK       ",
                             80: "ISO-IP         ",
                             81: "VMTP           ",
                             82: "SECURE-VMTP    ",
                             83: "VINES          ",
                             84: "TTP            ",
                             85: "NSFNET-IGP     ",
                             86: "DGP            ",
                             87: "TCF            ",
                             88: "EIGRP          ",
                             89: "OSPFIGP        ",
                             90: "Sprite-RPC     ",
                             91: "LARP           ",
                             92: "MTP            ",
                             93: "AX.25          ",
                             94: "IPIP           ",
                             95: "MICP           ",
                             96: "SCC-SP         ",
                             97: "ETHERIP        ",
                             98: "ENCAP          ",
                             100: "GMTP           ",
                             101: "IFMP           ",
                             102: "PNNI           ",
                             103: "PIM            ",
                             104: "ARIS           ",
                             105: "SCPS           ",
                             106: "QNX            ",
                             107: "A/N            ",
                             108: "IPComp         ",
                             109: "SNP            ",
                             110: "Compaq-Peer    ",
                             111: "IPX-in-IP      ",
                             112: "VRRP           ",
                             113: "PGM            ",
                             114: "               ",
                             115: "L2TP           ",
                             116: "DDX            ",
                             117: "IATP           ",
                             118: "STP            ",
                             119: "SRP            ",
                             120: "UTI            ",
                             121: "SMP            ",
                             122: "SM             ",
                             123: "PTP            ",
                             124: "ISIS over IPv4 ",
                             125: "FIRE           ",
                             126: "CRTP           ",
                             127: "CRUDP          ",
                             128: "SSCOPMCE       ",
                             129: "IPLT           ",
                             130: "SPS            ",
                             131: "PIPE           ",
                             132: "SCTP           ",
                             133: "FC             ",
                             134: "RSVP-E2E-IGNORE",
                             135: "Mobility Header",
                             136: "UDPLite        ",
                             137: "MPLS-in-IP     ",
                             138: "manet          ",
                             139: "HIP            ",
                             140: "Shim6          ", }
        for k in self.protocol_map:
            v = self.protocol_map[k]
            self.protocol_map[k] = v.strip()
        self.src_address = socket.inet_ntoa(struct.pack("<L", self.src))
        self.dst_address = socket.inet_ntoa(struct.pack("<L", self.dst))

        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except:
            self.protocol = str(self.protocol_num)


host = "192.168.2.195"
host = "192.168.4.126"
specify_sniffer_ip = '192.168.4.126'
host_black_list = []
host_black_list.append(host)
# 在线观看aiqiyi
host_black_list.append('192.168.4.142')
# heqing UPnP协议
host_black_list.append('192.168.4.151')
# ssdp协议
host_black_list.append('192.168.2.188')
host_black_list.append('192.168.2.191')
# DESKTOP-6HJOQK0  UPnP xubin
host_black_list.append('192.168.2.187')
host_black_list.append('192.168.2.195')
# litao
host_black_list.append('192.168.2.156')
# 交换机
host_black_list.append('192.168.1.1')
host_black_list.append('192.168.2.1')


dst_black_list = []
# 组播地址：239.255.255.250是SSDP(简单服务发现协议)，这是路由器的UPNP服务使用的协议。
dst_black_list.append('239.255.255.250')
dst_black_list.append('224.0.0.22')
dst_black_list.append('224.0.0.18')
dst_black_list.append('224.0.0.252')
dst_black_list.append('192.168.2.255')
dst_black_list.append('255.255.255.255')
dst_black_list.append('192.168.2.195')
dst_black_list.append('239.192.152.143')
dst_black_list.append('224.0.1.60')
dst_black_list.append('224.0.0.251')

protocol_black_list = []
protocol_black_list.append('ICMP')
# 移动互联网络控制程序
protocol_black_list.append("MOBILE")
# Microsoft网络的通讯协议
protocol_black_list.append("SHB")
# IP with Encryption
protocol_black_list.append("SWIPE")
# 集成网络层安全性 TUBA 53 SWIPE 采用加密的 IP
protocol_black_list.append("I-NLSP")

ip_host_name_map = {}

if os.name == "nt":
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
sniffer.bind((host, 33333))
# 设置在捕获的数据包中包含IP头
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
# 在WIN平台上，需要设置IOCTL以启用混杂模式
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

while True:
    date, addr = sniffer.recvfrom(65565)
    if not specify_sniffer_ip:
        if addr[0] in host_black_list:
            continue
    ip_header = IP(date[0:20])
    if specify_sniffer_ip:
        if ip_header.dst_address != specify_sniffer_ip and ip_header.src_address != specify_sniffer_ip:
            continue
    else:
        if ip_header.dst_address in dst_black_list:
            continue
        if ip_header.protocol in protocol_black_list:
            continue
    print '============================'

    try:
        src_host_name = ip_host_name_map.get(ip_header.src_address, None)
        if not src_host_name:
            src_host_name = socket.gethostbyaddr(ip_header.src_address)
    except:
        src_host_name = ''
    ip_host_name_map[ip_header.src_address] = src_host_name
    try:
        dst_host_name = ip_host_name_map.get(ip_header.dst_address, None)
        if not dst_host_name:
            dst_host_name = socket.gethostbyaddr(ip_header.dst_address)
    except:
        dst_host_name = ''
    ip_host_name_map[ip_header.dst_address] = dst_host_name
    print "Protocol:%s %s(%s) -> %s(%s)" \
          % (ip_header.protocol, ip_header.src_address,
             src_host_name, ip_header.dst_address, dst_host_name)
    print date[21:]
# 在WIN平台上关闭混杂模式
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
