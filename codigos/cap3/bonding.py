#!/usr/bin/python

from __future__ import print_function
import sys, os

from mininet.node import OVSKernelSwitch, Controller, RemoteController
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi


def topology(broadcast):
    "Create a network."
    if broadcast:
        net = Mininet_wifi(controller=Controller)
    else:
        net = Mininet_wifi(controller=RemoteController)

    info("*** Creating nodes\n")
    s1 = net.addSwitch('s1')
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    c1 = net.addController('c1')

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Associating...\n")
    net.addLink(s1, h1, bw=10)
    net.addLink(s1, h1, bw=10)
    net.addLink(s1, h2)
    net.addLink(s1, h3)

    info("*** Starting network\n")
    net.build()
    c1.start()
    s1.start([c1])

    if broadcast:
        h1.cmd('modprobe bonding mode=3')
    else:
        h1.cmd('modprobe bonding mode=4')
    h1.cmd('ip link add bond0 type bond')
    h1.cmd('ip link set bond0 address 00:00:00:11:22:33')
    h1.cmd('ip link set h1-eth0 down')
    h1.cmd('ip link set h1-eth0 address 00:00:00:00:00:11')
    h1.cmd('ip link set h1-eth0 master bond0')
    h1.cmd('ip link set h1-eth1 down')
    h1.cmd('ip link set h1-eth1 address 00:00:00:00:00:22')
    h1.cmd('ip link set h1-eth1 master bond0')
    h1.cmd('ip addr add 10.0.0.1/8 dev bond0')
    h1.cmd('ip addr del 10.0.0.1/8 dev h1-eth0')
    h1.cmd('ip link set bond0 up')

    info("*** Running CLI\n")
    CLI_wifi(net)

    os.system('rmmod bonding')

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    broadcast = True if '-b' in sys.argv else False
    topology(broadcast)
