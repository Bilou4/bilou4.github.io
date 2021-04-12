# DNS Spoofing

Can sometimes refer to DNS cache poisoning.
This refers to an attack where a host with no authority, directs a DNS and all its queries.

So an attacker can redirect all DNS queries to his own machine in order to steal data from the victim.


This is a LAN or WLAN attack, which is required for the attacker and victim to have the same network gateway.


## Ettercap Configuration

Edit the `/etc/ettercap/etter.conf` file. The lines to modify are


```text
ec_uid = 0
ec_gid = 0
```

Then there is a `Linux` part where you have to uncomment the lines about iptables (iptables v6 too).

Edit the `/etc/ettercap/etter.dns` file

This is the file that allows you to specify the redirection that will take place.

Under the tutorial, there are DNS records that you need to modify with the site you want to spoof and the IP address where the site is hosted (IP of the attacker in general).



## Ettercap

```sh
ettercap -G
```

Select the interface connected to the network and indicate not to start sniffing now. -> OK

> Hosts - Scan for hosts

Hosts Lists allows you to see the machines on the network.

You can use `nmap` to find the victim's address.

```sh
nmap [network_ip]
```

```sh
ip r # find the network gateway
```

Define targets

+ Target 1: victim
+ Target 2: gateway

## The attack

In the MITM menu select `ARP poisonning` and check `Sniff remote connections` -> OK

Plugins -> Manage plugins and choose dns_spoof to enable the plugin


You can start the apache2 service (one of the following commands)

``sh
service apache2 start
systemctl start apache2.service
```

Remember: the server files are in `/var/www/html`.


We can launch the attack: `Start Sniffing`


Now as soon as the victim visits the site indicated in etter.dns, they will be redirected to the attacker's site.

It is possible to detect if someone is using this technique on our network (https://null-byte.wonderhowto.com/how-to/tutorial-dns-spoofing-0167796)

