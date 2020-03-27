#!/usr/bin/python

# autor: Ramon dos Reis Fontes
# livro: Emulando Redes sem Fio com Mininet-WiFi
# github: https://github.com/ramonfontes/mn-wifi-book-pt

from mn_wifi.net import Mininet_wifi
from mn_wifi.node import OVSAP
from mn_wifi.cli import CLI
from mininet.node import  Controller
from mininet.log import setLogLevel, info


def topology():
    "Create a network."
    net = Mininet_wifi(controller=Controller, autoAssociation=False)

    info("*** Creating nodes\n")
    sta1 = net.addStation('sta1', position='10,60,0')
    sta2 = net.addStation('sta2', position='20,15,0')
    sta3 = net.addStation('sta3', position='10,25,0')
    sta4 = net.addStation('sta4', position='50,30,0')
    sta5 = net.addStation('sta5', position='45,65,0')
    ap1 = net.addAccessPoint('ap1', vssids=4, ssid=['ssid,ssid1,ssid2,ssid3,ssid4'],
                             mode="g", channel="1", position='30,40,0')
    c0 = net.addController('c0', controller=Controller)

    net.setPropagationModel(model='logDistance', exp=4)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    "plotting graph"
    net.plotGraph(max_x=100, max_y=100)

    info("*** Starting network\n")
    net.build()
    c0.start()
    ap1.start( [c0] )

    sta1.setRange(15)
    sta2.setRange(15)
    sta3.setRange(15)
    sta4.setRange(15)
    sta5.setRange(15)

    sta1.cmd('iw dev %s connect %s %s'
             % (sta1.params['wlan'][0], ap1.wintfs[1].ssid,
                ap1.wintfs[1].mac))
    sta2.cmd('iw dev %s connect %s %s'
             % (sta2.params['wlan'][0], ap1.wintfs[2].ssid,
                ap1.wintfs[2].mac))
    sta3.cmd('iw dev %s connect %s %s'
             % (sta3.params['wlan'][0], ap1.wintfs[2].ssid,
                ap1.wintfs[2].mac))
    sta4.cmd('iw dev %s connect %s %s'
             % (sta4.params['wlan'][0], ap1.wintfs[3].ssid,
                ap1.wintfs[3].mac))
    sta5.cmd('iw dev %s connect %s %s'
             % (sta5.params['wlan'][0], ap1.wintfs[4].ssid,
                ap1.wintfs[4].mac))

    ap1.cmd('ovs-ofctl add-flow ap1 in_port=2,actions=3')
    ap1.cmd('ovs-ofctl add-flow ap1 in_port=3,actions=2')
    ap1.cmd('ovs-ofctl add-flow ap1 in_port=4,actions=5')
    ap1.cmd('ovs-ofctl add-flow ap1 in_port=5,actions=4')

    info("*** Running CLI\n")
    CLI( net )

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()
