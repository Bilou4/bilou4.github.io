from typing import Dict
from diagrams import Diagram, Edge, Node
from diagrams.gcp.network import DNS
from diagrams.azure.network import DNSZones
from diagrams.onprem.client import User

class EdgeRequest(Edge):
    def __init__(
        self,
        node: Node = None,
        forward: bool = False,
        reverse: bool = False,
        label: str = "",
        color: str = "",
        style: str = "",
        **attrs: Dict
    ):
        color = "blue"
        super().__init__(node, forward, reverse, label, color, style, **attrs)


class EdgeResponse(Edge):
    def __init__(
        self,
        node: Node = None,
        forward: bool = False,
        reverse: bool = False,
        label: str = "",
        color: str = "",
        style: str = "",
        **attrs: Dict
    ):
        color = "orange"
        style = "dotted"
        super().__init__(node, forward, reverse, label, color, style, **attrs)



def generate_graph_how_dns_work():
    graph_attr = {
        "bgcolor": "transparent",
        "splines": "polyline",
    }

    with Diagram(
        "How DNS requests work?",
        filename="src/it/attacks/dns/img/how_dns_work",
        outformat="png",
        direction="LR",
        graph_attr=graph_attr,
        show=False,
    ):
        user = User("User")
        recursive_dns = DNS("Recursive DNS")

        root_dns = DNSZones("DNS")
        first_domain_dns = DNSZones("DNS")
        tld_dns = DNSZones("DNS")

        user >> EdgeRequest(label="(1) bilou4.github.io") >> recursive_dns
        recursive_dns >> EdgeRequest(label="(2) bilou4.github.io") >> root_dns
        recursive_dns >> EdgeRequest(label="(4) bilou4.github.io") >> first_domain_dns
        recursive_dns >> EdgeRequest(label="(6) bilou4.github.io") >> tld_dns

        root_dns >> EdgeResponse(label="(3) servers list *.io") >> recursive_dns
        (
            first_domain_dns
            >> EdgeResponse(label="(5) servers list *.github.io")
            >> recursive_dns
        )
        tld_dns >> EdgeResponse(label="(7) IP address") >> recursive_dns
        recursive_dns >> EdgeResponse(label="(8) IP address") >> user
