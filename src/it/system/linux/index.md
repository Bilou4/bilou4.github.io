# Linux

## Namespace

This is the basis of docker. It allows you to simulate a network on your machine.

```bash
ip netns
ip netns add <NAME>
ip netns exec <NAME> <COMMAND> # execute a command in another namespace
```


## Command line tips

### Self-signed certificate

```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes
```


### awk

#### From timestamp to human readable date

```bash
TZ=Ameria/Los_Angeles awk '/path to look for/' { print strftime ("%T", $1), $3, $7} file.log
```