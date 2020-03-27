#!/usr/bin/python

# autor: Ramon dos Reis Fontes
# livro: Emulando Redes sem Fio com Mininet-WiFi
# github: https://github.com/ramonfontes/mn-wifi-book-pt

from mininet.node import Controller
from mininet.log import setLogLevel, info
from mn_wifi.node import UserAP
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology():
    "Create a network."
    net = Mininet_wifi(controller=Controller, accessPoint=UserAP)

    info("*** Creating nodes\n")
    sta1 = net.addStation('sta1', passwd='123456789a', encrypt='wpa2')
    sta2 = net.addStation('sta2')
    ap1 = net.addAccessPoint('ap1', ssid="ap1-ssid", mode="g", channel="1",
                             passwd='123456789a', encrypt='wpa2', failMode="standalone")

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Associating Stations\n")
    net.addLink(sta1, ap1)

    info("*** Starting network\n")
    net.build()
    ap1.start([])

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()
