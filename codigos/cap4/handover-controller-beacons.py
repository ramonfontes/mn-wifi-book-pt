#!/usr/bin/python

from mininet.node import RemoteController, UserSwitch
from mininet.log import setLogLevel, info
from mn_wifi.node import UserAP
from mn_wifi.link import wmediumd
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi
from mn_wifi.wmediumdConnector import interference


def topology():
    "Create a network."
    net = Mininet_wifi(controller=RemoteController, accessPoint=UserAP, switch=UserSwitch,
                       link=wmediumd, wmediumd_mode=interference)

    info("*** Creating nodes\n")
    sta1 = net.addStation('sta1', position='15,20,0')
    sta2 = net.addStation('sta2', position='35,20,0')
    ap1 = net.addAccessPoint('ap1', mac='00:00:00:00:00:01', ssid="handover",
                             mode="g", channel="1", passwd='123456789a',
                             encrypt='wpa2', position='10,30,0')
    ap2 = net.addAccessPoint('ap2', mac='00:00:00:00:00:02', ssid="handover",
                             mode="g", channel="6", passwd='123456789a',
                             encrypt='wpa2', position='60,30,0')
    ap3 = net.addAccessPoint('ap3', mac='00:00:00:00:00:03', ssid="handover",
                             mode="g", channel="1", passwd='123456789a',
                             encrypt='wpa2', position='120,100,0')
    s4 = net.addSwitch('s4')
    h1 = net.addHost('h1')
    controller_ = net.addHost('con', ip='10.0.0.100/8', inNamespace=False)
    c1 = net.addController('c1', controller=RemoteController, ip='127.0.0.1')

    info("*** Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=3.5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    net.plotGraph(max_x=300, max_y=300)

    info("*** Creating links\n")
    net.addLink(h1, ap1)
    net.addLink(s4, ap1)
    net.addLink(s4, ap2)
    net.addLink(s4, ap3)
    net.addLink(s4, controller_)

    info("*** Starting network\n")
    net.build()
    net.addNAT().configDefault()
    c1.start()
    ap1.start([c1])
    ap2.start([c1])
    ap3.start([c1])
    s4.start([c1])

    sta1.cmd('iw dev sta1-wlan0 interface add mon0 type monitor')
    sta1.cmd('ifconfig mon0 up')
    sta2.cmd('iw dev sta2-wlan0 interface add mon0 type monitor')
    sta2.cmd('ifconfig mon0 up')
    sta1.cmd('wpa_cli -i sta1-wlan0 roam 00:00:00:00:00:01')
    sta2.cmd('wpa_cli -i sta2-wlan0 roam 00:00:00:00:00:01')
    sta1.cmd('./sta1_1.py &')
    sta2.cmd('./sta2_1.py &')

    info("*** Running CLI\n")
    CLI_wifi(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()
