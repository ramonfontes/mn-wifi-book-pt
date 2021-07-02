#!/usr/bin/python

# autor: Ramon dos Reis Fontes
# livro: Emulando Redes sem Fio com Mininet-WiFi
# github: https://github.com/ramonfontes/mn-wifi-book-pt

import os

from mininet.log import setLogLevel, info
from mininet.node import Controller
from mn_wifi.net import Mininet_wifi
from mn_wifi.cli import CLI
from mn_wifi.replaying import ReplayingNetworkConditions
from sys import version_info as py_version_info


def topology():
    "Create a network."
    net = Mininet_wifi( controller=Controller )

    info("*** Creating nodes")
    sta1 = net.addStation( 'sta1', mac='00:00:00:00:00:01',
                           ip='192.168.0.1/24',
                           position='47.28,50,0' )
    sta2 = net.addStation( 'sta2', mac='00:00:00:00:00:02',
                           ip='192.168.0.2/24',
                           position='54.08,50,0' )
    ap3 = net.addAccessPoint( 'ap3', ssid='ap-ssid3', mode='g',
                              channel='1', position='50,50,0' )
    c0 = net.addController('c0', controller=Controller, port=6653)

    info("*** Configuring wifi nodes")
    net.configureWifiNodes()

    info("*** Starting network")
    net.build()
    c0.start()
    ap3.start( [c0] )

    sta1.cmd('iw dev sta1-wlan0 interface add mon0 type monitor &')
    sta1.cmd('ifconfig mon0 up &')
    sta2.cmd('iw dev sta2-wlan0 interface add mon0 type monitor &')
    sta2.cmd('ifconfig mon0 up &')
    if py_version_info < (3, 0):
        sta2.cmd('pushd ~/Downloads; python -m SimpleHTTPServer 80 &')
    else:
        sta2.cmd('pushd ~/Downloads; python -m http.server 80 &')

    path = os.path.dirname(os.path.abspath(__file__))
    getTrace(sta1, '%s/replayingNetworkConditions/clientTrace.txt' % path)
    getTrace(sta2, '%s/replayingNetworkConditions/serverTrace.txt' % path)

    replayingNetworkConditions.addNode(sta1)
    replayingNetworkConditions.addNode(sta2)
    replayingNetworkConditions(net)

    info("*** Running CLI")
    CLI( net )

    info("*** Stopping network")
    net.stop()

def getTrace(sta, file):

    file = open(file, 'r')
    raw_data = file.readlines()
    file.close()

    sta.time = []
    sta.bw = []
    sta.loss = []
    sta.delay = []
    sta.latency = []

    for data in raw_data:
        line = data.split()
        sta.time.append(float(line[0])) #First Column = Time
        sta.bw.append(((float(line[1]))/1000000)/2) #Second Column = BW
        sta.loss.append(float(line[2])) #second Column = LOSS
        sta.latency.append(float(line[3])) #Second Column = LATENCY

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()
