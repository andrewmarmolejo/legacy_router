#!/usr/bin/python
# File: legacy_router.py

###     IMPORTS
from mininet.net import Mininet
from mininet.node import Host, Node
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost
from mininet.nodelib import LinuxBridge #OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.link import TCLink, Intf
from subprocess import call

###     NETWORK FUNCTION
def myNetwork():
    
    net = Mininet( topo=None,
                   build=False,
                   ipBase='192.168.1.1/24')

    info( '*** Adding controller\n' )
    info( '*** Add switches\n')
    
    #   CREATES GLOBAL HOST r1
    r1 = net.addHost('r1', cls=Node, ip='0.0.0.0')
    #   IP FORWARDING
    r1.cmd('sysctl -w net.ipv4.ip_forward=1')

    #   ADDS HOSTS TO INTERACT
    info( '*** Add hosts\n')
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    
    #   ADDS LINKS TO h1 & h2
    info( '*** Add links\n')
    net.addLink(h1, r1 intName2=)
    net.addLink(h2, r1)

    info( '*** Starting network\n')
    net.build()

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
