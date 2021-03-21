# Network sniffing

**Concept:** Interception of traffic (packets), then packet analysis, decoding of packets if necessary. Information retrieval => URL, user name, mdp...

## Tools

### Ettercap

Tools for Man in the Middle attacks on a LAN. Ettercap is able to perform attacks on the ARP protocol to position itself as 'Man in the Middle'. This subsequently allows:
* infect, replace and delete data in a connection
* discover mdp's for protocols such as FTP, HTTP, POP, SSH...
* Provide victims with fake SSL certificates in HTTPS sessions

```sh
ettercap -G # run in graphical mode
```
> `-> Sniff -> Unified sniffing` => start a scan

> `-> Hosts -> Hosts list -> Hosts scan` => Get machines

> Select a target machine -> Mitm(man in the middle) -> ARP Poisoning -> sniff remote connections

### Wireshark (formerly ethereal)

Free packet analyzer. It is used for troubleshooting and analysis of computer networks, protocol development, education and reverse engineering.



