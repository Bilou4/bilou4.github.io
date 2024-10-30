# Linux

## Namespace

This is the basis of docker. It allows you to simulate a network on your machine.

```bash
ip netns
ip netns add <NAME>
ip netns exec <NAME> <COMMAND> # execute a command in another namespace
```


## Mount/Unmount

*following commands must be run as root*

```bash
fdisk -l # view the disk and the partition

/dev/sd?  -> physical disk
/dev/sda? -> partitions on the sda disk
```

### Mounting on `/mnt/data`

```bash
mkdir -p /mnt/data # create an empty dir
parted -l # determine the filesystem type
mount -t <ext4> /dev/sd /mnt/data
```

### Unmounting

The argument is either the mount point  or the name of the disk

```bash
umount /dev/sdb
umount /mnt/data
```

## Shell redirection

```bash
/dev/null # empty, import anything, it will disappear
/dev/zero # endless zeros
/dev/urandom # endless random numbers
/dev/full # file that always returns the error code ENOSPC (No space left on device)

# following ones are links to the kernel file descriptor
/dev/stdin # standard input stream 			# 0
/dev/stdout # standard output stream		# 1
/dev/stderr # standard error output stream  # 2
```

### Redirects

By default, it redirects stdout.

- `>` is an overwrite method
- `>>` is an append method

Following lines are equivalent

```bash
echo "Hello, World!" > file.txt
echo "Hello, World!" 1> file.txt
```

- `>&` is the syntax for redirecting the stream to a file descriptor.

```bash
# redirecting stderr to stdout
ls file-that-does-not-exist 2>&1 # if no '&' the file named "1" will be created
```

Redirect `stdout` and `stderr` to the same place

```bash
ls -la /tmp /dir-that-does-not-exist 1>file.txt 2>&1
cat file.txt
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

### Traffic control - TC

*tc must be run as root*

**qdiscs** (queuing discipline - modify the scheduler) buffer between the protocol stack and the network interface. By default, it uses a FIFO approach.

**filter** determines which classful qdisc a packet should be enqueued to. (Can qualify the packet based on things like: source/destination/IP...)

**classes** a class is a sub-qdisc. A class may contains another class. Using classes, we can configure the QoS in more detail.

```bash
# delay to the egress (outgoing packets) scheduler
tc qdisc add dev eth0 root netem delay 200ms
# delay = the network property to modify
# netem = network emulator (emulate a WAN property)
```

**Example**

```bash
$ ping -c 4 google.com
PING google.com ..... 56(84) bytes of data.
64 bytes from ..... : icmp_seq=1 ttl=116 time=9.86 ms
64 bytes from ..... : icmp_seq=2 ttl=116 time=12.2 ms
64 bytes from ..... : icmp_seq=3 ttl=116 time=11.3 ms
64 bytes from ..... : icmp_seq=4 ttl=116 time=10.5 ms

--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 8ms
rtt min/avg/max/mdev = 9.859/10.971/12.185/0.870 ms
$ tc qdisc add dev eth0 root netem delay 200ms # add some delay
$ ping -c 4 google.com
PING google.com ..... 56(84) bytes of data.
64 bytes from ..... : icmp_seq=1 ttl=116 time=210 ms
64 bytes from ..... : icmp_seq=2 ttl=116 time=210 ms
64 bytes from ..... : icmp_seq=3 ttl=116 time=211 ms
64 bytes from ..... : icmp_seq=4 ttl=116 time=210 ms

--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 7ms
rtt min/avg/max/mdev = 209.870/210.072/210.585/0.546 ms
```

```bash
tc qdisc del dev eth0 root # delete all rules
# instead of del or add, possible values are: show (see what are default rules), change
tc disc change dev eth0 root netem delay 200ms 10ms # +/- 10ms uniform distribution
# instead of delay, possible values are: 'loss 10%' (packet loss of 10%), corrupt, duplicate.
```

**Bandwidth limit**

```bash
tc qdisc add dev eth0 root tbf rate 1mbit burst 32kbit latency 400ms
# tbf: token buffer to manipulate traffic rates
# rate: sustained max rate
# burst: max allowed burst
# latency: packets with higher latency get dropped


$ iperf -c speedtest.serverius.net -p 5002
------------------------------------------------------------
Client connecting to speedtest.serverius.net, TCP port 5002
TCP window size: 85.0 KByte (default)
------------------------------------------------------------
[  3] local 192.168.1.15 port 60442 connected with 178.21.16.76 port 5002
write failed: Broken pipe
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0- 0.1 sec  84.8 KBytes  12.6 Mbits/sec
$ sudo tc qdisc add dev eth0 root tbf rate 1mbit burst 32kbit latency 400ms
$ iperf -c speedtest.serverius.net p 5002
------------------------------------------------------------
Client connecting to speedtest.serverius.net, TCP port 5002
TCP window size: 85.0 KByte (default)
------------------------------------------------------------
[  3] local 192.168.1.15 port 43834 connected with 178.21.16.76 port 5002
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.3 sec  1.38 MBytes  1.12 Mbits/sec
```


### Exiftool

#### Rename images to their creation/modification date attributes

```bash
exiftool -ext jpg '-FileName<CreateDate' -d %Y%m%d_%H%M%S%%-c.%%e current_filename.jpg
# -d: specify a date format Y=year m=month d=day H=hours M=minutes S=seconds
# %-c: add a counter if multiple images have the same name.
# %%e: keep the extension

exiftool -ext jpg '-FileName<filemodifydate' -d %Y%m%d_%H%M%S%%-c.%%e ./some-directory
# it will execute the command on all images inside the directory
```