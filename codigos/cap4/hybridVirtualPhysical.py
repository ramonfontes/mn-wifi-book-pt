#!/usr/bin/python

# autor: Ramon dos Reis Fontes
# livro: Emulando Redes sem Fio com Mininet-WiFi
# github: https://github.com/ramonfontes/mn-wifi-book-pt

from mininet.log import setLogLevel, info
from mininet.node import Controller
from mn_wifi.node import OVSAP, physicalAP
from mn_wifi.net import Mininet_wifi
from mn_wifi.cli import CLI_wifi
from mn_wifi.link import wmediumd
from mn_wifi.wmediumdConnector import interference


def topology():
    "Create a network."
    net = Mininet_wifi( controller=Controller )

    usbDongleIface = 'wlxf4f26d193319'

    info("*** Creating nodes\n")
    sta1 = net.addStation('sta1', mac='00:00:00:00:00:01',
                          ip='192.168.0.1/24', position='10,10,0')
    phyap1 = net.addAccessPoint('phyap1', ssid='ssid-ap1',
                                mode='g', channel='1',
                                position='50,50,0', phywlan=usbDongleIface,
                                cls=physicalAP)
    c0 = net.addController( 'c0' )

    info("*** Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=3.5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    net.plotGraph(max_x=240, max_y=240)

    info("*** Starting network\n")
    net.build()
    c0.start()
    phyap1.start( [c0] )

    info("*** Running CLI\n")
    CLI_wifi( net )

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()
