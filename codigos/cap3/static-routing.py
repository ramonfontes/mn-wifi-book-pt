#!/usr/bin/python

from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi


def topology():
    "Create a network."
    net = Mininet_wifi()

    info("*** Creating nodes\n")
    sta1 = net.addStation('sta1', ip='192.168.0.1/24')
    sta2 = net.addStation('sta2', ip='192.168.1.1/24')
    r1 = net.addStation('r1')
    r2 = net.addStation('r2')

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    r1.setMasterMode(intf='r1-wlan0', ssid='r1-ssid',
                     channel='1', mode='n')
    r2.setMasterMode(intf='r2-wlan0', ssid='r2-ssid',
                     channel='1', mode='n')

    info("*** Creating Links\n")
    net.addLink(r1, r2)

    info("*** Starting network\n")
    net.build()

    r1.cmd('sysctl net.ipv4.ip_forward=1')
    r2.cmd('sysctl net.ipv4.ip_forward=1')
    r1.cmd('ifconfig r1-wlan0 192.168.0.100')
    r1.cmd('ifconfig r1-eth2 10.0.0.1')
    r2.cmd('ifconfig r2-wlan0 192.168.1.100')
    r2.cmd('ifconfig r2-eth2 10.0.0.2')
    r1.cmd('ip route add to 192.168.1.1 via 10.0.0.2')
    r2.cmd('ip route add to 192.168.0.1 via 10.0.0.1')
    sta1.cmd('iw dev sta1-wlan0 connect r1-ssid')
    sta2.cmd('iw dev sta2-wlan0 connect r2-ssid')
    sta1.cmd('route add default gw 192.168.0.100')
    sta2.cmd('route add default gw 192.168.1.100')

    info("*** Running CLI\n")
    CLI_wifi(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()
