#!/usr/bin/python

from mn_wifi.net import Mininet_wifi
from mn_wifi.node import OVSAP
from mn_wifi.cli import CLI_wifi
from mininet.node import  Controller
from mininet.log import setLogLevel, info


def topology():
    "Create a network."
    net = Mininet_wifi( controller=Controller, autoAssociation=False )

    info("*** Creating nodes\n")
    sta1 = net.addStation( 'sta1', position='10,60,0' )
    sta2 = net.addStation( 'sta2', position='20,15,0' )
    sta3 = net.addStation( 'sta3', position='10,25,0' )
    sta4 = net.addStation( 'sta4', position='50,30,0' )
    sta5 = net.addStation( 'sta5', position='45,65,0' )
    ap1 = net.addAccessPoint( 'ap1', vssids=4, ssid="ssid,ssid1,ssid2,ssid3,ssid4",
                              mode="g", channel="1", position='30,40,0' )
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

    sta1.cmd('iwconfig sta1-wlan0 essid %s ap %s' %
             (ap1.params['ssid'][1], ap1.params['mac'][1]))
    sta2.cmd('iwconfig sta2-wlan0 essid %s ap %s' %
             (ap1.params['ssid'][2], ap1.params['mac'][2]))
    sta3.cmd('iwconfig sta3-wlan0 essid %s ap %s' %
             (ap1.params['ssid'][2], ap1.params['mac'][2]))
    sta4.cmd('iwconfig sta4-wlan0 essid %s ap %s' %
             (ap1.params['ssid'][3], ap1.params['mac'][3]))
    sta5.cmd('iwconfig sta5-wlan0 essid %s ap %s' %
             (ap1.params['ssid'][4], ap1.params['mac'][4]))

    ap1.cmd('ovs-ofctl add-flow ap1 in_port=2,actions=3')
    ap1.cmd('ovs-ofctl add-flow ap1 in_port=3,actions=2')
    ap1.cmd('ovs-ofctl add-flow ap1 in_port=4,actions=5')
    ap1.cmd('ovs-ofctl add-flow ap1 in_port=5,actions=4')

    info("*** Running CLI\n")
    CLI_wifi( net )

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()
