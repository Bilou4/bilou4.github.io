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

### Creating large files from your terminal

The `dd` command will create a sparse file.

```bash
dd if=/dev/urandom of=your-filename bs=2G count=1
# bs = block size (1M = 1024Mb)
# count = number of blocks
```

The `fallocate` command will not create a sparse file, which means it is much faster.
```bash
fallocate -l 1G your-filename
```