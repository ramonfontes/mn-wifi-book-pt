#!/usr/bin/python

from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi


def topology():
    "Create a network."
    net = Mininet_wifi(controller=Controller)

    info("*** Creating nodes\n")
    net.addStation('sta1', mac='00:00:00:00:00:02', ip='10.0.0.2/8', position='20,50,0')
    net.addStation('sta2', mac='00:00:00:00:00:03', ip='10.0.0.3/8', position='25,50,0')
    net.addStation('sta3', mac='00:00:00:00:00:04', ip='10.0.0.4/8', position='35,50,0')
    net.addStation('sta4', mac='00:00:00:00:00:05', ip='10.0.0.5/8', position='40,50,0')
    net.addStation('sta5', mac='00:00:00:00:00:06', ip='10.0.0.6/8', position='45,50,0')
    ap1 = net.addAccessPoint('ap1', ssid='ssid-ap1', mode='g', channel='1',
                             position='50,50,0')
    ap2 = net.addAccessPoint('ap2', ssid='ssid-ap2', mode='g', channel='6',
                             position='70,50,0', range=30)
    c1 = net.addController('c1')

    net.setPropagationModel(model="logDistance", exp=5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    net.setAssociationCtrl('ssf')

    info("*** Associating and Creating links\n")
    net.addLink(ap1, ap2)

    net.plotGraph(max_x=120, max_y=120)

    info("*** Starting network\n")
    net.build()
    c1.start()
    ap1.start([c1])
    ap2.start([c1])

    info("*** Running CLI\n")
    CLI_wifi(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()
