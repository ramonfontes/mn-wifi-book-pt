#!/usr/bin/python

from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.node import OVSKernelAP
from mn_wifi.link import wmediumd
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi
from mn_wifi.wmediumdConnector import interference


def topology():
    "Create a network."
    net = Mininet_wifi(controller=Controller, link=wmediumd,
                       accessPoint=OVSKernelAP, wmediumd_mode=interference,
                       noise_threshold=-91, fading_coefficient=3)

    info("*** Creating nodes\n")
    ap1 = net.addAccessPoint('ap1', ssid='ap1', mode='n',
                             channel='1', position='15,30,0')
    ap2 = net.addAccessPoint('ap2', ssid='ap2', mode='n',
                             channel='6', position='35,30,0')
    ap3 = net.addAccessPoint('ap3', ssid='ap3', mode='n',
                             channel='11', position='55,30,0')
    net.addStation('sta1', mac='00:00:00:00:00:10', ip='10.0.0.1/8',
                   position='30,30,0')

    info("*** Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    net.plotGraph(max_x=100, max_y=100)

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
    topology()
