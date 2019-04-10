#!/usr/bin/python

# autor: Ramon dos Reis Fontes
# livro: Emulando Redes sem Fio com Mininet-WiFi
# github: https://github.com/ramonfontes/mn-wifi-book-pt

from mininet.node import RemoteController, UserSwitch
from mininet.log import setLogLevel, info
from mn_wifi.node import UserAP
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi
from mn_wifi.link import wmediumd
from mn_wifi.wmediumdConnector import interference
import os


def topology():
    "Create a network."
    net = Mininet_wifi(link=wmediumd, wmediumd_mode=interference)

    info("*** Creating nodes\n")
    net.addStation( 'sta1', ip='192.168.0.1',
                    radius_passwd='sdnteam', encrypt='wpa2',
                    radius_identity='joe', position='110,120,0' )
    net.addStation( 'sta2', ip='192.168.0.2',
                    radius_passwd='hello', encrypt='wpa2',
                    radius_identity='bob', position='200,100,0' )
    ap1 = net.addStation( 'ap1', ip='192.168.0.100',
                          position='150,100,0' )
    h1 = net.addHost('h1', ip='10.0.0.100/8')
    s1 = net.addSwitch('s1')
    c0 = net.addController('c0', controller=RemoteController,
                           ip='127.0.0.1', port=6653 )

    info("*** Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=3.5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    ap1.setMasterMode(intf='ap1-wlan0', ssid='ap1-ssid', channel='1',
                      mode='n', authmode='8021x', encrypt='wpa2',
                      radius_server='10.0.0.100')

    info("*** Associating Stations\n")
    net.addLink(ap1, s1)
    net.addLink(s1, h1)

    info("*** Starting network\n")
    net.build()
    c0.start()
    s1.start([c0])

    ap1.cmd('ifconfig ap1-eth2 10.0.0.200')
    ap1.cmd('ifconfig ap1-wlan0 0')

    h1.cmdPrint('rc.radiusd start')
    ap1.cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')
#    s1.cmd('ovs-ofctl add-flow s1 in_port=1,priority=65535,'
 #           'dl_type=0x800,nw_proto=17,tp_dst=1812,actions=2,controller')

    info("*** Running CLI\n")
    CLI_wifi(net)

    os.system('pkill radiusd')

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()
