#!/usr/bin/python

import sys

from mininet.node import Controller, RemoteController
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi


def topology(qos):
    "Create a network."
    net = Mininet_wifi(controller=RemoteController)

    info("*** Creating nodes\n")
    sta1 = net.addStation('sta1', position='10,10,0')
    h1 = net.addHost('h1')
    ap1 = net.addAccessPoint('ap1', ssid="simplewifi", position='10,20,0',
                             mode="g", channel="5", protocols='OpenFlow13', datapath='user')
    c0 = net.addController('c0')

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Associating Stations\n")
    net.addLink(sta1, ap1)
    net.addLink(h1, ap1)

    info("*** Starting network\n")
    net.build()
    c0.start()
    ap1.start([c0])

    if qos:
        ap1.cmdPrint('ovs-ofctl -O OpenFlow13 add-meter ap1 '
                     '\'meter=1,kbps,bands=type=drop,rate=5000\'')
        ap1.cmdPrint('ovs-ofctl -O OpenFlow13 add-flow ap1 '
                     '\'priority=1,in_port=1 action=meter:1,2\'')
        ap1.cmdPrint('ovs-ofctl -O OpenFlow13 add-flow ap1 '
                     '\'priority=1,in_port=2 action=meter:1,1\'')

    info("*** Running CLI\n")
    CLI_wifi(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    qos = True if '-q' in sys.argv else False
    topology(qos)
