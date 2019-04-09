"""router topology example

chain of routers between two hosts

   h1---r1---r2-...-rN---h2

Subnets are 10.0.0 to 10.0.N
The last IPv4 address byte (host byte) is 2 on the left and 1 on the right, for routers. 
ri-eth0 is the interface on the left and ri-eth1 is on the right. IPv4 addresses look like:
   10.0.[k-1].2--r[k]--10.0.k.1

"""

from mininet.net import Mininet
from mininet.node import Node, OVSKernelSwitch, Controller, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.topo import Topo
from mininet.log import setLogLevel, info
import argparse

ENABLE_LEFT_TO_RIGHT_ROUTING = True		# tell all routers how to get to h2
ENABLE_RIGHT_TO_LEFT_ROUTING = True		# ditto for h1
ENABLE_RIP = True				# enable RIPv2; rip.py must be in same directory

class LinuxRouter( Node ):	# from the Mininet library
    "A Node with IP forwarding enabled."

    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        info ('enabling forwarding on ', self)
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()


class RTopo(Topo):
    def __init__(self, **kwargs):
#    def build(self, **_kwargs):     # special names?
        super(RTopo, self).__init__(**kwargs)
        for key in kwargs:
           if key == 'N': N=kwargs[key]

        h1 = self.addHost( 'h1', ip=ip(0,10,24), defaultRoute='via '+ ip(0,2) )
        h2 = self.addHost( 'h2', ip=ip(N,10,24), defaultRoute='via '+ ip(N,1) )
 
	rlist = []

        for i in range(1,N+1):
            ri = self.addHost('r'+str(i), cls=LinuxRouter)
            rlist.append(ri)

        self.addLink( h1, rlist[0], intfName1 = 'h1-eth0', intfName2 = 'r1-eth0')

        for i in range(1,N):  # link from ri to r[i+1]
            self.addLink(rlist[i-1], rlist[i], inftname1 = 'r'+str(i)+'-eth1', inftname2 = 'r'+str(i+1)+'-eth0')
 
        self.addLink( rlist[N-1], h2, intfName1 = 'r'+str(N)+'-eth1', intfName2 = 'h2-eth0')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-N', '--N', type=int)
    args = parser.parse_args()
    if args.N is None: N = 3
    else: N = args.N
    rtopo = RTopo(N=N)

    net = Mininet(topo = rtopo, link=TCLink, autoSetMacs = True)
    net.start()

    # now configure the router IPv4 addresses, using the ip() function below
    for i in range(1, N+1):
        r = net['r'+str(i)]
        left_intf  = 'r'+str(i)+'-eth0'
        right_intf = 'r'+str(i)+'-eth1'
        r.cmd('ifconfig ' + left_intf + ' ' + ip(i-1, 2, 24))
        r.cmd('ifconfig ' + right_intf + ' ' +ip(i,   1, 24))
        rp_disable(r)

    h1 = net['h1']
    h2 = net['h2']
    h1.cmd('/usr/sbin/sshd')
    h2.cmd('/usr/sbin/sshd')
    for i in range(1, N+1):
        r = net['r'+str(i)]
        r.cmd('/usr/sbin/sshd')
        if ENABLE_RIP: r.cmd('python3 rip.py &')

    if ENABLE_LEFT_TO_RIGHT_ROUTING:
        for i in range(1,N):
            r = net['r'+str(i)]
            right_intf = 'r' + str(i) + '-eth1'
            r.cmd('ip route add to ' + ip(N,0,24) + ' via ' + ip(i,2) + ' dev ' + right_intf)

    # ONE-WAY routing from h2 to h1
    if ENABLE_RIGHT_TO_LEFT_ROUTING:
        for i in range(2,N+1):
           r = net['r'+str(i)]
           left_intf = 'r' + str(i) + '-eth0'
           r.cmd('ip route add to ' + ip(0,0,24) + ' via ' + ip(i-1,1) + ' dev ' + left_intf)

    CLI( net)
    net.stop()

# The following generates IP addresses from a subnet number and a host number
# ip(4,2) returns 10.0.4.2, and ip(4,2,24) returns 10.0.4.2/24
def ip(subnet,host,prefix=None):
    addr = '10.0.'+str(subnet)+'.' + str(host)
    if prefix != None: addr = addr + '/' + str(prefix)
    return addr

# For some examples we need to disable the default blocking of forwarding of packets with no reverse path
def rp_disable(host):
    ifaces = host.cmd('ls /proc/sys/net/ipv4/conf')
    ifacelist = ifaces.split()    # default is to split on whitespace
    for iface in ifacelist:
       if iface != 'lo': host.cmd('sysctl net.ipv4.conf.' + iface + '.rp_filter=0')


setLogLevel('info')	# 'info' is normal; 'debug' is for when there are problems
main()

"""
Manual routing commands for N=3

r1: ip route add to 10.0.3.0/24 via 10.0.1.2 dev r1-eth1
r2: ip route add to 10.0.3.0/24 via 10.0.2.2 dev r2-eth2

r1: route add -net 10.0.3.0/24 gw 10.0.1.2
r2: route add -net 10.0.3.0/24 gw 10.0.2.2

r3: ip route add to 10.0.0.0/24 via 10.0.2.1 dev r3-eth0
r2: ip route add to 10.0.0.0/24 via 10.0.1.1 dev r2-eth0

r3: route add -net 10.0.0.0/24 gw 10.0.2.1
r2: route add -net 10.0.0.0/24 gw 10.0.1.1

"""

