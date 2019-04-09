#!/usr/bin/python

import sys

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi
from mn_wifi.node import OVSBridgeAP


def topology(stp):

    net = Mininet_wifi(accessPoint=OVSBridgeAP)

    info("*** Creating nodes\n")
    sta1 = net.addStation('sta1', mac='00:00:00:00:00:02', ip='10.0.0.1/8',
                          position='100,101,0')
    sta2 = net.addStation('sta2', mac='00:00:00:00:00:03', ip='10.0.0.2/8',
                          position='50,51,0')
    sta3 = net.addStation('sta3', mac='00:00:00:00:00:04', ip='10.0.0.3/8',
                          position='150,51,0')
    if stp:
        ap1 = net.addAccessPoint('ap1', ssid='new-ssid1', mode='g', channel='1',
                                 failMode="standalone", position='100,100,0',
                                 stp=True)
        ap2 = net.addAccessPoint('ap2', ssid='new-ssid2', mode='g', channel='1',
                                 failMode="standalone", position='50,50,0',
                                 stp=True)
        ap3 = net.addAccessPoint('ap3', ssid='new-ssid3', mode='g', channel='1',
                                 failMode="standalone", position='150,50,0',
                                 stp=True)
    else:
        ap1 = net.addAccessPoint('ap1', ssid='new-ssid1', mode='g', channel='1',
                                 failMode="standalone", position='100,100,0')
        ap2 = net.addAccessPoint('ap2', ssid='new-ssid2', mode='g', channel='1',
                                 failMode="standalone", position='50,50,0')
        ap3 = net.addAccessPoint('ap3', ssid='new-ssid3', mode='g', channel='1',
                                 failMode="standalone", position='150,50,0')

    net.setPropagationModel(model="logDistance", exp=4.5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Creating links\n")
    net.addLink(ap1, sta1)
    net.addLink(ap2, sta2)
    net.addLink(ap3, sta3)
    net.addLink(ap1, ap2)
    net.addLink(ap1, ap3)
    net.addLink(ap2, ap3)

    net.plotGraph(max_x=300, max_y=300)

    info("*** Starting network\n")
    net.build()
    ap1.start([])
    ap2.start([])
    ap3.start([])

    info("*** Running CLI\n")
    CLI_wifi(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    stp = True if '-s' in sys.argv else False
    topology(stp)
