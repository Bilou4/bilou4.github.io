# DNS


![How DNS work](./img/how_dns_work.png)

1. The computer sends (through the stub resolver) the request to the recursive DNS server of its configuration
2. The recursive DNS server sends successively its request to 3 DNS levels
3. Solicitation of a root DNS. There are 13 of them with a unique IP. It sends back to the recursive DNS, the addresses of the servers managing the resolution of the 1st level domain (Ex: .io)
4. Solicitation of a TLD server managing the top level domain
5. Response containing the addresses of the servers managing the TLD (Ex: github.io)
6. Solicitation of the server managing github.io
7. The server provides the IP to reach bilou4.github.io
8. The recursive DNS server provides this IP to the computer


<u>stub resolver</u>: library or DNS component of the computer. It receives DNS requests from the computer's applications and communicates them to the recursive server present in the network interface settings. Sometimes a cache can be present to increase performance (Ex: systemd, systemd-resolv)

<u>Recursive DNS server</u>: It does not have DNS information as such. It gets DNS resolution by querying other DNS types. It has a cache.

<u>Root DNS</u>: There are 13 of them and their IP address is stored in the recursive DNS. They respond to recursive DNS by providing the address of TLD servers.

<u>Top Level Domain</u>: These servers have the names and addresses of all authoritative DNS servers for a domain name under the top level domain they manage.

<u>DNS authority on a DNS domain</u>: this is the DNS server that holds all DNS entries attached to the domain name being resolved


## Network risks

1. <u>Privacy loss</u>: DNS queries are in clear. It can be intercepted and modified (content injection) or blocked (censorship)
2. <u>compromise responses</u>: DNS queries are poorly signed (DNSsec allows the client to verify that the response comes from an authority. This protects against injection but not inspection or censorship).
3. <u>unavailability</u>: an attacker can block a computer's connection to a recursive DNS. The goal of the attack would be to respond faster than the legitimate response with a fake DNS resolution.

### Protection

Currently, there is no solution to encrypt between recursive DNS and DNS authorities but 2 protocols exist:
- Dns Over Tls
- Dns Over Https

<u>Stubby</u>: is a tool to encrypt queries between the client and the recursive DNS. It contains a list of DOT servers in its default configuration. ⚠️ may have performance impacts.
