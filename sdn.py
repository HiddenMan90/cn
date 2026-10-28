from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info


def create_sdn_topology():
    net = Mininet(
        controller=Controller,
        switch=OVSKernelSwitch
    )

    info("*** Adding Controller\n")
    net.addController("c0")

    info("*** Adding OpenFlow Switches\n")
    s1 = net.addSwitch("s1", protocols="OpenFlow13")
    s2 = net.addSwitch("s2", protocols="OpenFlow13")

    info("*** Adding Hosts\n")
    h1 = net.addHost(
        "h1", ip="10.0.0.1/24",
        mac="00:00:00:00:00:01"
    )
    h2 = net.addHost(
        "h2", ip="10.0.0.2/24",
        mac="00:00:00:00:00:02"
    )
    h3 = net.addHost(
        "h3", ip="10.0.0.3/24",
        mac="00:00:00:00:00:03"
    )
    h4 = net.addHost(
        "h4", ip="10.0.0.4/24",
        mac="00:00:00:00:00:04"
    )

    info("*** Creating Links\n")
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s2)
    net.addLink(h4, s2)
    net.addLink(s1, s2)

    info("*** Starting Network\n")
    net.start()

    info("*** Testing Network Connectivity\n")
    net.pingAll()

    info("*** Running Mininet CLI\n")
    CLI(net)

    info("*** Stopping Network\n")
    net.stop()


if __name__ == "__main__":
    setLogLevel("info")
    create_sdn_topology()
