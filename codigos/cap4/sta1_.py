#!/usr/bin/python

from scapy.all import *
import os

def pkt_callback(pkt):
    broadcast = "ff:ff:ff:ff:ff:ff"
    addr1 = "02:00:00:00:00:00"
    if pkt.haslayer(Dot11):
        extra = pkt.notdecoded
        signal = -(256 - ord(extra[-4:-3]))
        if str(pkt.addr1) == addr1:
            msg = "vehicle: %s / transmitter: %s / signal: %s" % (pkt.addr1, pkt.addr2, signal)
            packet = IP(src="10.0.0.1", dst="10.0.0.100")/TCP(sport=8000, dport=6653)/msg
            send(packet, verbose=0)

sniff(iface="mon0", prn=pkt_callback)
